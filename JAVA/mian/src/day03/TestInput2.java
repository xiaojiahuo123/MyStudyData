package day03;

import java.util.Scanner;

public class TestInput2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        /*
        next()，nextInt()，nextDouble()，nextBoolean()等
        它们从控制台读取数据的规则是 从当前输入光标开始  往右找第1个非空格的字符开始读取，直到遇到空格、换行等空白字符位置。
        柴林燕              18  85.6  女

        next()从 柴前面开始读取，读取完柴林燕遇到空格就结束，光标停留在燕的后面
        nextInt()从燕的后面开始找第1个非空格的字符1开始读取，读完18遇到空格就结束，光标停留在8的后面
        nextDouble()从8的后面开始找第1个非空格的字符8开始读取，读完85.6遇到空格就结束，光标停留在6的后面
        next()从6的后面开始找第1个非空格的字符女开始读取，读完女遇到换行就结束，光标停留在女的后面
         */
        System.out.print("请输入姓名 年龄 体重 性别：");
        String name = input.next();
        int age = input.nextInt();
        double weight = input.nextDouble();
        char gender = input.next().charAt(0);
//        next()返回的是 String 类型。所以需要将 String 转换为 char。charAt(0)是 String 类的方法，用于获取字符串中索引为 0 的字符，
//        也就是第一个字符。
        System.out.println("name = " + name);
        System.out.println("age = " + age);
        System.out.println("weight = " + weight);
        System.out.println("gender = " + gender);

        input.close();
    }
}
