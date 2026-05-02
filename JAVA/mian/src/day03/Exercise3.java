package day03;

import java.util.Scanner;

public class Exercise3 {
    public static void main(String[] args) {
        /*
        3、假设你想开发一个玩彩票的游戏，程序随机地产生一个两位数的彩票，提示用户输入一个两位数，然后按照下面的规则判定用户是否能赢。
        // 1) 如果用户输入的数匹配彩票的实际顺序，奖金10 000美元。
        if (randNum == inputNum) {
            System.out.println("奖金 10000 美元");
        }
        2)如果用户输入的所有数字匹配彩票的所有数字，但顺序不一致，奖金 3 000美元。
        3)如果用户输入的一个数字仅满足顺序情况下匹配彩票的一个数字，奖金1 000美元。
        4)如果用户输入的一个数字仅满足非顺序情况下匹配彩票的一个数字，奖金500美元。
        5)如果用户输入的数字没有匹配任何一个数字，则彩票作废。
         */
        //随机产生一个两位数：[10,99] 或 [10,100)
        /*
        方式一：Math.random()
        Math.random() 得到[0,1)范围的小数值
        [a,b)范围的数
        Math.random() * (b-a) + a
        Math.random() * 90  [0,90)范围的小数
        Math.random() * 90 + 10 [10,100)范围的小数
        (int)(Math.random() * 90 + 10)
         */
        int randNum = (int)(Math.random() * 90 + 10);


        /*
        方式二：Random类
         */
        /*Random r = new Random();
        int randNum2 = r.nextInt(10, 100);
        System.out.println("randNum2 = " + randNum2);*/

        Scanner input = new Scanner(System.in);

        System.out.print("请输入一个2位数：");
        int inputNum = input.nextInt();

        int randNumShi = randNum / 10;
        int randNumGe = randNum % 10;
        int inputNumShi = inputNum /10;
        int inputNumGe = inputNum % 10;

        if(randNum == inputNum){
            System.out.println("奖金 10000");
        }else if(randNumShi == inputNumGe && randNumGe == inputNumShi){
            System.out.println("奖金3000");
        }else if(randNumShi == inputNumShi || randNumGe == inputNumGe){
            System.out.println("奖金1000");
        }else if(randNumShi == inputNumGe || randNumGe == inputNumShi){
            System.out.println("奖金500");
        }else{
            System.out.println("谢谢惠顾！");
        }
        System.out.println("本次中奖号码： " + randNum);

        input.close();
    }
}
