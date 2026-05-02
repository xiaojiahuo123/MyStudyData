package day03;

import java.util.Scanner;

public class Exercise4_3 {
    public static void main(String[] args) {
        //4、编写程序：由键盘输入三个整数分别存入变量num1、num2、num3，实现从小到大输出三个整数。
        Scanner input = new Scanner(System.in);

        System.out.print("请输入3个整数（空格分割）：");
        int num1 = input.nextInt();
        int num2 = input.nextInt();
        int num3 = input.nextInt();

        /*
        3个数排序的方法有很多种：
        方案三：排列组合
        num1 <= num2 <= num3
        num1 <= num3 <= num2
        num2 <= num1 <= num3
        num2 <= num3 <= num1
        num3 <= num1 <= num2
        num3 <= num2 <= num1
         */
        if(num1<=num2 && num2<=num3){
            System.out.println(num1 + "<=" +  num2 + "<=" +  num3);
        }else if(num1<=num3 && num3<=num2){
            System.out.println(num1 + "<=" +  num3 + "<=" +  num2);
        }else if(num2<=num1 && num1<=num3){
            System.out.println(num2 + "<=" +  num1 + "<=" +  num3);
        }else if(num2<=num3 && num3<=num1){
            System.out.println(num2 + "<=" +  num3 + "<=" +  num1);
        }else if(num3<=num2 && num2<=num1){
            System.out.println(num3 + "<=" +  num2 + "<=" +  num1);
        }else{
            System.out.println(num3 + "<=" +  num1 + "<=" +  num2);
        }

        input.close();
    }
}
