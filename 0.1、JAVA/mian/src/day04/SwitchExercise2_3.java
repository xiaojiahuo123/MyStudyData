package day04;

import java.util.Scanner;

public class SwitchExercise2_3 {
    public static void main(String[] args) {
        /*
        赌数游戏：随机产生3个1-6的整数，如果三个数相等，那么称为“豹子”，如果三个数之和大于9，称为“大”，
        如果三个数之和小于等于9，称为“小”，用户从键盘输入押的是“豹子”、“大”、“小”，并判断是否猜对了
         */

        //随机产生3个1-6的整数
        //方式一：Math.random() 产生[a,b)的整数 (int)(Math.random()*(b-a) + a)
        //方式二：Random工具类的nextInt(a,b)
        int x = (int) (Math.random() * (7 - 1) + 1);
        int y = (int) (Math.random() * (7 - 1) + 1);
        int z = (int) (Math.random() * (7 - 1) + 1);

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

        boolean result = switch (guess) {
            case "豹子" -> x == y && y == z;
            case "大" -> x + y + z > 9;
            case "小" -> x + y + z <= 9;
            default -> false;
        };

        System.out.println(result ? "猜对了" : "猜错了");

        input.close();
    }
}
