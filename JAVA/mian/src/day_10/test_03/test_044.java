package day_10.test_03;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.time.Duration;
import java.util.HashSet;
import java.util.Set;
//爬取小说内容，这是不管格式的版本
public class test_044 {
    // 目标网站的基础URL（用户会直接提供具体的小说内容URL）
    private static final String BASE_URL = "https://www.cool18.com/bbs4/index.php?app=forum&act=threadview&tid=14444055";
    // 超时时间设置为30秒（增加超时时间）
    private static final HttpClient client = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(30))
            .build();
    // 存储已访问的URL，避免重复爬取
    private static final Set<String> visitedUrls = new HashSet<>();
    // 最大重试次数
    private static final int MAX_RETRIES = 3;
    // 重试间隔（毫秒）
    private static final int RETRY_INTERVAL_MS = 2000;

    /**
     * 获取指定URL的页面内容，添加重试机制
     */
    private static String fetchPageContent(String url) {
        int retries = 0;
        while (retries < MAX_RETRIES) {
            try {
                HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create(url))
                        .timeout(Duration.ofSeconds(30))
                        .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
                        .header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
                        .header("Accept-Language", "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2")
                        .header("Referer", "https://www.cool18.com/")
                        .GET()
                        .build();

                HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

                if (response.statusCode() == 200) {
                    return response.body();
                } else {
                    System.err.println("获取页面失败，状态码: " + response.statusCode() + "，URL: " + url);
                    if (retries == MAX_RETRIES - 1) {
                        return null;
                    }
                }
            } catch (IOException | InterruptedException e) {
                System.err.println("获取页面内容时出错: " + e.getMessage() + "，URL: " + url + "，尝试第 " + (retries + 1) + " 次");
                if (retries == MAX_RETRIES - 1) {
                    return null;
                }
            }

            retries++;
            try {
                System.out.println("等待 " + RETRY_INTERVAL_MS + " 毫秒后重试...");
                Thread.sleep(RETRY_INTERVAL_MS);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        try {
            // 直接爬取用户提供的具体小说内容页面
            String novelContentUrl = BASE_URL;
            String htmlContent = fetchPageContent(novelContentUrl);

            if (htmlContent != null) {
                System.out.println("成功获取小说页面内容，开始解析...");

                // 解析页面，提取小说标题
                Document doc = Jsoup.parse(htmlContent);
                // 提取小说标题 - 添加空值检查和更通用的选择器
                String novelTitle = "未知小说";
                Element titleElement = doc.selectFirst("h1.subject-title");
                if (titleElement == null) {
                    // 尝试其他可能的标题选择器
                    titleElement = doc.selectFirst("h1");
                }
                if (titleElement == null) {
                    titleElement = doc.selectFirst("title");
                }
                if (titleElement != null) {
                    novelTitle = titleElement.text();
                }
                System.out.println("正在爬取小说: " + novelTitle);

                // 直接爬取当前页面的小说内容
                System.out.println("直接爬取当前页面的小说内容...");

                // 创建存储小说内容的字符串构建器
                StringBuilder novelContent = new StringBuilder();
                novelContent.append(novelTitle).append("\n\n");

                // 爬取当前页面的小说内容
                String novelTextContent = fetchChapterContent(novelContentUrl);
                if (novelTextContent != null && !novelTextContent.trim().isEmpty()) {
                    novelContent.append(novelTextContent).append("\n\n");

                    // 输出前200个字符作为预览
                    String preview = novelTextContent.length() > 200
                            ? novelTextContent.substring(0, 200) + "..."
                            : novelTextContent;
                    System.out.println("小说内容预览: " + preview);
                }

                // 保存小说内容到文件
                saveNovelToFile(novelTitle, novelContent.toString());
                System.out.println("\n小说爬取完成！已保存为文件。");
            }
        } catch (Exception e) {
            System.err.println("爬取过程中发生错误: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * 爬取单个帖子（小说）内容 - 适配cool18.com的论坛结构
     */
    private static String fetchChapterContent(String url) {
        try {
            String htmlContent = fetchPageContent(url);
            if (htmlContent == null) {
                return null;
            }

            Document doc = Jsoup.parse(htmlContent);
            // 根据cool18.com论坛结构优化内容选择器
            Element contentElement = null;

            // 尝试多种可能的内容选择器，适配cool18.com的论坛结构
            // 1. 尝试查找帖子内容区域
            contentElement = doc.selectFirst("div.bbs-content");

            // 2. 尝试查找文章内容区域
            if (contentElement == null) {
                contentElement = doc.selectFirst("div.article-content");
            }

            // 3. 尝试查找主内容区域
            if (contentElement == null) {
                contentElement = doc.selectFirst("div.content");
            }

            // 4. 尝试查找ID为content的元素
            if (contentElement == null) {
                contentElement = doc.selectFirst("div#content");
            }

            // 5. 尝试查找帖子正文区域（根据论坛特点添加）
            if (contentElement == null) {
                contentElement = doc.selectFirst("div.post-content");
            }

            // 6. 尝试查找具有特定class的内容区域
            if (contentElement == null) {
                contentElement = doc.selectFirst("div[class*=content]");
            }

            // 7. 尝试查找包含段落的主区域（最后手段）
            if (contentElement == null) {
                Elements paragraphs = doc.select("p");
                if (!paragraphs.isEmpty()) {
                    // 创建一个临时元素来容纳所有段落
                    contentElement = doc.createElement("div");
                    for (Element p : paragraphs) {
                        contentElement.appendChild(p.clone());
                    }
                }
            }

            if (contentElement != null) {
                // 清理内容，移除不需要的元素（如广告、导航等）
                Elements unwantedElements = contentElement.select("script, style, div.ad, a, img, form, input, button, iframe");
                unwantedElements.remove();

                // 获取纯文本内容并处理格式
                String textContent = contentElement.text();
                // 替换多余的空白字符为单个换行
                textContent = textContent.replaceAll("\\s{3,}", "\n\n");

                // 进一步清理文本，移除可能的论坛标记和干扰内容
                textContent = textContent.trim();
                if (textContent.length() > 100) { // 确保内容足够长，避免提取到非正文内容
                    return textContent;
                } else {
                    System.out.println("提取的内容过短，可能不是完整小说内容");
                    return null;
                }
            } else {
                System.out.println("未能找到章节内容，请检查内容选择器是否正确");
                return null;
            }
        } catch (Exception e) {
            System.err.println("解析章节内容时出错: " + e.getMessage());
            return null;
        }
    }

    /**
     * 将小说内容保存到文件
     */
    private static void saveNovelToFile(String title, String content) {
        try {
            // 处理文件名，移除特殊字符
            String safeTitle = title.replaceAll("[\\/:*?\"<>|]", "_");

            // 创建保存目录
            Path saveDir = Paths.get("novels");
            if (!Files.exists(saveDir)) {
                Files.createDirectories(saveDir);
            }

            // 保存文件
            Path filePath = saveDir.resolve(safeTitle + ".txt");
            Files.writeString(filePath, content, StandardCharsets.UTF_8,
                    StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);

            System.out.println("小说已保存至: " + filePath.toAbsolutePath());
        } catch (IOException e) {
            System.err.println("保存小说到文件时出错: " + e.getMessage());
        }
    }
}



