package day04;

import java.util.Scanner;

public class TestLoop2 {
    public static void main(String[] args) {
        //随机产生1个[0,100)的整数，然后你来猜
        //如果猜的数 大于 随机产生的数，提醒玩家，猜大了
        //如果猜的数 小于 随机产生的数，提醒玩家，猜小了
        //如果猜的数 小于 随机产生的数，恭喜猜中了

        int randNum = (int)(Math.random()*100);
        Scanner input = new Scanner(System.in);

        //至少猜1次
/*        int num;
        do{
            System.out.print("请猜：");
            num = input.nextInt();

            if(num > randNum){
                System.out.println("猜大了");
            }else if(num < randNum){
                System.out.println("猜小了");
            }else{
                System.out.println("猜中了");
            }
        }while(num != randNum);*/

       /* int num = -1;//这里初始化为-1，是为了让第一次while循环成立
        while(num != randNum){
            System.out.print("请猜：");
            num = input.nextInt();

            if(num > randNum){
                System.out.println("猜大了");
            }else if(num < randNum){
                System.out.println("猜小了");
            }else{
                System.out.println("猜中了");
            }
        }*/

        for( int num = -1; num != randNum; ){
            System.out.print("请猜：");
            num = input.nextInt();

            if(num > randNum){
                System.out.println("猜大了");
            }else if(num < randNum){
                System.out.println("猜小了");
            }else{
                System.out.println("猜中了");
            }
        }

        input.close();
    }
}
