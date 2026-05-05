package day03;

import java.util.Scanner;

public class Exercise4 {
    public static void main(String[] args) {
        //4、编写程序：由键盘输入三个整数分别存入变量num1、num2、num3，实现从小到大输出三个整数。
        Scanner input = new Scanner(System.in);

        System.out.print("请输入3个整数（空格分割）：");
        // 使用Scanner对象的nextInt()方法从键盘读取整数
        // nextInt()会读取用户输入的下一个整数（以空格、回车等分隔）
        // 将读取到的整数依次赋值给num1、num2、num3三个变量
        int num1 = input.nextInt();  // 读取第一个整数并存储到num1变量中
        int num2 = input.nextInt();  // 读取第二个整数并存储到num2变量中
        int num3 = input.nextInt();  // 读取第三个整数并存储到num3变量中

        /*
        3个数排序的方法有很多种：
        方案一：先找出最大，再找出最小的，最后确定中间的
         */
        int max = num1 > num2 ? num1 : num2;
        max = max > num3 ? max : num3;
        System.out.println("max = " + max);

        int min = num1 < num2 ? num1 : num2;
        min = min < num3 ? min : num3;
        System.out.println("min = " + min);

        int middle = num1 + num2 + num3 - max - min;
        System.out.println("middle = " + middle);

        System.out.println(min + "<=" + middle + "<=" + max);


        input.close();
    }
}
