package day03;

import java.util.Scanner;

public class TestIf {
    public static void main(String[] args) {
        //定义一个变量，用于存储一年的总天数
        int days = 365;

        //从控制台读取键盘输入的年份值
        Scanner input = new Scanner(System.in);

        System.out.print("请输入年份：");
        int year = input.nextInt();

        //判断year是不是闰年，如果是闰年，请把days变量修改为366
        //(1)年份可以被4整除同时不被100整除（2）年份可以被400整除
        if(year % 4 == 0 && year % 100 != 0 || year % 400 == 0){
            days = 366;
        }

        //输出结果
        System.out.println(year +"年共有" + days + "天");

        input.close();
    }
}
