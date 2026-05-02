package day04;

import java.util.Scanner;

public class TestSwitchCase2 {
    public static void main(String[] args) {
        /*
        从控制台接收用户输入的年、月、日，然后计算这一天是这一年的第几天，
        例如：输入的是2024-11-6
        (1)计算1-10月的满月天数
        (2)加11月的6天
         */
        Scanner input = new Scanner(System.in);

        System.out.print("请输入年 月 日：");
        int year = input.nextInt();
        int month = input.nextInt();
        int day = input.nextInt();

        //定义一个变量，用来存总天数
        int days = 0;

        //先计算[1, month-1]月的满月天数
        /*if(month==2){
            days += 31;//1月的满月天数
        }else if(month == 3){
            days += 31 + (year%4==0 && year%100!=0 || year%400==0 ? 29 : 28);//1,2月总天数
        }else if(month == 4){
            days += 31 + (year%4==0 && year%100!=0 || year%400==0 ? 29 : 28) + 31;//1,2,3月总天数
        }//这么写比较麻烦*/
        switch (month){
            case 12:
                days += 30;//11月的满月天数
            case 11:
                days += 31;//10月的满月天数
            case 10:
                days += 30;//9月的满月天数
            case 9:
                days += 31;//8月的满月天数
             case 8:
                days += 31;//7月的满月天数
            case 7:
                days += 30;//6月的满月天数
            case 6:
                days += 31;//5月的满月天数
            case 5:
                days += 30;//4月的满月天数
            case 4:
                days += 31;//3月的满月天数
            case 3:
                days += year%4==0 && year%100!=0 || year%400==0 ? 29 : 28;//2月的满月天数
            case 2:
                days += 31;//1月的满月天数
            case 1:
                days += day;
        }
        System.out.println(year +"年" + month +"月" + day + "日是这一年的第" + days +"天");


        input.close();
    }
}
