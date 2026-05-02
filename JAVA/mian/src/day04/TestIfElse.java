package day04;

import java.util.Scanner;

public class TestIfElse {
    public static void main(String[] args) {
        //从控制台接收用户输入的星期值[1,7]，然后输出它对应的英文单词
        Scanner input = new Scanner(System.in);

        System.out.print("请输入星期值[1,7]：");
        int week = input.nextInt();

        //快速格式化的快捷键：Ctrl + Alt + l
        if (week == 1) {
            System.out.println("Monday");
        } else if (week == 2) {
            System.out.println("Tuesday");
        } else if (week == 3) {
            System.out.println("Wednesday");
        } else if (week == 4) {
            System.out.println("Thursday");
        } else if (week == 5) {
            System.out.println("Friday");
        } else if (week == 6) {
            System.out.println("Saturday");
        } else if (week == 7) {
            System.out.println("Sunday");
        } else {
            System.out.println("星期输入有误");
        }


        input.close();
    }
}
