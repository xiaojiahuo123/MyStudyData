package day07_teacher_code.src;

import java.util.Scanner;

public class TestMethod {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("请输入一个单字符：");
//        char c = input.nextChar();
        //这里报错的原因是因为Scanner类中没有声明nextChar()方法

        input.close();
    }
}
