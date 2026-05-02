package day04;

import java.util.Scanner;

public class SwitchExercise2 {
    public static void main(String[] args) {
        /*
        赌数游戏：随机产生3个1-6的整数，如果三个数相等，那么称为“豹子”，如果三个数之和大于9，称为“大”，
        如果三个数之和小于等于9，称为“小”，用户从键盘输入押的是“豹子”、“大”、“小”，并判断是否猜对了
         */

        //随机产生3个1-6的整数
        //方式一：Math.random() 产生[a,b)的整数 (int)(Math.random()*(b-a) + a)
        //方式二：Random工具类的nextInt(a,b)
        int x = (int)(Math.random() * (7-1) + 1);
        int y = (int)(Math.random() * (7-1) + 1);
        int z = (int)(Math.random() * (7-1) + 1);

/*        Random random = new Random();
        int x = random.nextInt(1,7);
        int y = random.nextInt(1,7);
        int z = random.nextInt(1,7);*/

        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);

        Scanner input = new Scanner(System.in);
        System.out.print("请押宝（豹子、大、小）:");
        String guess = input.next();
        System.out.println("guess = " + guess);

        String randStr = "";
        if(x == y && y == z){
            randStr = "豹子";
        }else if(x + y + z > 9){
            randStr = "大";
        }else{
            randStr = "小";
        }
        System.out.println("randStr = " + randStr);

        /*if(guess == randStr){//对于字符串来说，不能用==字符串的内容，因为字符串不是基本数据类型
            System.out.println("猜对了");
        }else{
            System.out.println("猜错了");
        }*/
        if(guess.equals(randStr)){
            System.out.println("猜对了");
        }else{
            System.out.println("猜错了");
        }

        input.close();
    }
}
