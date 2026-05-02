package day05_teacher_code.src;

import java.util.Random;

public class MyLianxi_03 {
    // 验证码字符集：包含大小写字母和数字
    private static final String CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    // 验证码长度
    private static final int CODE_LENGTH = 6;

    public static void main(String[] args) {
//      案例需求：随机生成一组验证码，验证码由大小写字母和10个阿拉伯数字字符中的任意6位组成。
        char[] VerificationCode = new char[62];
        //Verification Code  验证码
                // 生成并打印验证码
                String verificationCode = generateVerificationCode();
                System.out.println("生成的验证码: " + verificationCode);
    }

    /**
     * 生成随机验证码
     * @return 6位长度的随机验证码字符串
     */
    public static String generateVerificationCode() {
        // 创建随机数生成器
        Random random = new Random();
        // 创建字符串构建器用于拼接验证码字符
        StringBuilder codeBuilder = new StringBuilder();

        // 循环生成6个随机字符
        for (int i = 0; i < CODE_LENGTH; i++) {
            // 从字符集中随机选择一个字符的索引
            int index = random.nextInt(CHARACTERS.length());
            // 获取对应索引的字符并添加到验证码中
            codeBuilder.append(CHARACTERS.charAt(index));
        }

        return codeBuilder.toString();
    }
}
