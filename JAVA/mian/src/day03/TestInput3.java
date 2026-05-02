package day03;

import java.util.Scanner;

public class TestInput3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        /*
        next()，nextInt()，nextDouble()，nextBoolean()等
        它们从控制台读取数据的规则是 从当前输入光标开始  往右找第1个非空格的字符开始读取，直到遇到空格、换行等空白字符位置。
        nextLine()，从当前输入光标开始一直读取，包括空格，直到遇到回车换行为止
         */
        System.out.print("请输入姓名 年龄 体重 性别：");
        String name = input.nextLine();//小心
        int age = input.nextInt();
        double weight = input.nextDouble();
        char gender = input.next().charAt(0);

        System.out.println("name = " + name);
        System.out.println("age = " + age);
        System.out.println("weight = " + weight);
        System.out.println("gender = " + gender);

        input.close();
    }
}
