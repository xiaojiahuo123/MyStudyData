package day05_teacher_code.src;

import java.util.Scanner;

public class ArrayExercise4_2 {
    public static void main(String[] args) {
        /*
        （1）已知平年12个月每个月的总天数是{ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31}，
        （2）从键盘输入年，月，日，分别用year，month，day变量接收
        （3）计算这一天是这一年的第几天。
        （4）提示：闰年的判断标准
        - 年份year可以被4整除，但不能被100整除
        - 或年份year可以被400整除
         */
        //(1)定义/声明1个数组，把平年12个月的天数存起来
        int[] daysOfMonth = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31};

        //(2)从键盘输入年，月，日，分别用year，month，day变量接收
        Scanner input = new Scanner(System.in);

        System.out.print("请输入年：");
        int year = input.nextInt();

        System.out.print("请输入月：");
        int month = input.nextInt();

        System.out.print("请输入日：");
        int day = input.nextInt();

        //(3)计算这一天是这一年的第几天
        //例如：输入的是2024年12月2日
        //A：[1,11]月满月天数
        //B：第12月的2天
/*        int days = 0;
        days += day; //B：第12月的2天*/
        int days = day;//B：第12月的2天

        //用循环累加[1,month-1]月的总天数，例如A：[1,11]月满月天数
        for(int i=1; i<month; i++){
            days += daysOfMonth[i-1];

            //(4)考虑闰年
            //当月份是2月，才需要考虑闰年的事
            if(i==2 && (year%4==0 && year%100!=0 || year%400==0)){
                days++;
            }
        }


        System.out.println(year +"-" +month +"-" + day +"是这一年的第" + days);

        input.close();

    }
}
