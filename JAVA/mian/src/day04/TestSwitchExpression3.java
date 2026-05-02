package day04;

import java.util.Scanner;

public class TestSwitchExpression3 {
    public static void main(String[] args) {
        //从控制台接收用户输入的星期值[1,7]，然后输出它对应的英文单词
        Scanner input = new Scanner(System.in);

        System.out.print("请输入星期值[1,7]：");
        int week = input.nextInt();

        String weekName = switch (week) {
            case 1 -> "Monday";
            case 2 -> "Tuesday";
            case 3 -> "Wednesday";
            case 4 -> "Thursday";
            case 5 -> "Friday";
            case 6 -> "Saturday";
            case 7 -> {
                System.out.println("这一天是我最喜欢的一天！");
                yield "Sunday";//yield是一个上下文关键字，只在switch表达式的内部是关键字，在其他地方是普通单词
            }
            default -> "星期输入有误";
        };
        System.out.println("weekName = " + weekName);

        input.close();
    }
}
