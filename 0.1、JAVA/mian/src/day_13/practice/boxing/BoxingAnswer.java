package day_13.practice.boxing;

public class BoxingAnswer {
    // Q1 编程题答案：判断Integer是否为偶数
    public static boolean isEven(Integer num) {
        if (num == null) return false;
        return num % 2 == 0;
    }
    // Q2 理解题答案：
    // Integer i = 128; Integer j = 128; i == j结果为false，因为超过了Integer缓存范围（-128~127），i和j是不同对象。
}
