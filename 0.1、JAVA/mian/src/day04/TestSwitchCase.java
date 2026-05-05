package day04;

import java.util.Scanner;

public class TestSwitchCase {
    public static void main(String[] args) {
        //从控制台接收用户输入的星期值[1,7]，然后输出它对应的英文单词
        Scanner input = new Scanner(System.in);

        System.out.print("请输入星期值[1,7]：");
        int week = input.nextInt();

        switch (week){
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("这一天是我最喜欢的一天！");
                System.out.println("这一天是我最喜欢的一天！");
                System.out.println("这一天是我最喜欢的一天！");
                System.out.println("Sunday");
                break;
            default:
                System.out.println("星期输入有误");
                break;
        }







        input.close();
    }
}
