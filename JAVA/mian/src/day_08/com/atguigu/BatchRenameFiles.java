package day_08.com.atguigu;

import java.io.File;
import java.util.Scanner;

public class BatchRenameFiles {

    // 需要删除的广告文本
    private static String adTextToRemove = "【海量资源：kebaiwan.net】";
    // 根文件夹路径
    private static String rootFolderPath = "E:\\Code\\711.2025年3月尚硅谷Java+AI大模型应用开发革新版本";

    public static void main(String[] args) {
        BatchRenameFiles renamer = new BatchRenameFiles();

        // 获取用户输入确认
        Scanner scanner = new Scanner(System.in);
        System.out.println("即将处理文件夹: " + renamer.rootFolderPath);
        System.out.println("将从文件名中删除的内容: " + adTextToRemove);
        System.out.print("确认继续? (y/n): ");
        String confirm = scanner.nextLine();

        if (confirm.equalsIgnoreCase("y")) {
            File rootFolder = new File(renamer.rootFolderPath);

            if (!rootFolder.exists() || !rootFolder.isDirectory()) {
                System.out.println("错误: 文件夹不存在或不是有效的文件夹路径");
                return;
            }

            // 开始处理文件
            renamer.processFiles(rootFolder);
            System.out.println("处理完成!");
        } else {
            System.out.println("操作已取消");
        }

        scanner.close();
    }

    /**
     * 递归处理文件夹中的所有文件和子文件夹
     */
    private void processFiles(File folder) {
        // 获取文件夹中的所有文件和子文件夹
        File[] files = folder.listFiles();

        if (files == null) {
            return; // 如果无法访问该文件夹，直接返回
        }

        for (File file : files) {
            if (file.isDirectory()) {
                // 如果是文件夹，递归处理
                processFiles(file);
            } else {
                // 如果是文件，处理文件名
                renameFile(file);
            }
        }
    }

    /**
     * 重命名文件，删除文件名中的广告文本
     */
    private void renameFile(File file) {
        String originalName = file.getName();
        // 分离文件名和扩展名
        int dotIndex = originalName.lastIndexOf('.');
        String fileNameWithoutExt;
        String extension = "";

        if (dotIndex > 0) {
            fileNameWithoutExt = originalName.substring(0, dotIndex);
            extension = originalName.substring(dotIndex);
        } else {
            fileNameWithoutExt = originalName;
        }

        // 移除广告文本
        String newFileNameWithoutExt = fileNameWithoutExt.replace(adTextToRemove, "");
        String newFileName = newFileNameWithoutExt + extension;

        // 如果文件名有变化才进行重命名
        if (!newFileName.equals(originalName)) {
            File newFile = new File(file.getParent(), newFileName);

            // 处理可能的重名情况
            int counter = 1;
            while (newFile.exists()) {
                newFileName = newFileNameWithoutExt + "_" + counter + extension;
                newFile = new File(file.getParent(), newFileName);
                counter++;
            }

            // 执行重命名
            boolean renamed = file.renameTo(newFile);
            if (renamed) {
                System.out.println("已重命名: " + originalName + " -> " + newFileName);
            } else {
                System.out.println("重命名失败: " + originalName);
            }
        }
    }
}
    