package day03;

import java.util.Scanner;

public class Exercise4_2 {
    public static void main(String[] args) {
        //4、编写程序：由键盘输入三个整数分别存入变量num1、num2、num3，实现从小到大输出三个整数。
        Scanner input = new Scanner(System.in);

        System.out.print("请输入3个整数（空格分割）：");
        int num1 = input.nextInt();
        int num2 = input.nextInt();
        int num3 = input.nextInt();

        /*
        3个数排序的方法有很多种：
        方案二：冒泡排序法
        3个数用2轮：
        第一轮：
            num1 > num2 交换  确保 num1 < num2
            num2 > num3 交换  确保 num2 < num3
         第二轮：
              num1 > num2 交换  确保 num1 < num2
        目标：num1 <= num2 <= num3
         */
        if(num1 > num2){
            int temp = num1;
            num1 = num2;
            num2 = temp;
        }
        if(num2 > num3){
            int temp = num2;
            num2 = num3;
            num3 = temp;
        }

        if(num1 > num2){
            int temp = num1;
            num1 = num2;
            num2 = temp;
        }

        System.out.println(num1 +"<=" + num2 + "<=" + num3);

        input.close();
    }
}
