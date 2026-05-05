package day03;

import java.util.Scanner;

public class TestIfElse {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("请输入一个整数：");
        int num = input.nextInt();

        /*if(num % 2 == 0){
            System.out.println(num + "是偶数");
        }
        if(num % 2 != 0){
            System.out.println(num +"是奇数");
        }*/

        if(num % 2 == 0){
            System.out.println(num + "是偶数");
        }else{
            System.out.println(num +"是奇数");
        }

        input.close();
    }
}
