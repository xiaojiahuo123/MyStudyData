package day05_teacher_code.src;

import java.util.Scanner;

public class ArrayExercise2 {
    public static void main(String[] args) {
        /*
        （1）用一个数组，保存星期一到星期天的7个英语单词，数组如下：
            {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"}
        （2）从键盘输入1-7的整数，显示该整数对应的单词
         */

        //(1)用一个数组，保存星期一到星期天的7个英语单词
        //单词肯定是字符串String
        String[] arr = {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"};

//        (2)从键盘输入1-7的整数
        Scanner input = new Scanner(System.in);

/*        int week;
        while (true) {
            //选中要用xx包围的代码，按快捷键Ctrl + Alt + T，选择一个结构包围
            System.out.print("请输入星期值[1,7]：");
            week = input.nextInt();

            if(week >=1 && week <= 7){
                break;
            }else{
                System.out.println("星期输入有误！星期值是[1,7]范围！");
            }
        }*/

        System.out.print("请输入星期值[1,7]：");
        int week = input.nextInt();

        System.out.println(week +"对应的单词是" + arr[week-1]);//因为下标是[0,6]


        input.close();
    }
}
