package day04;

import java.util.Scanner;

public class ForExercise4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double balance = 0.0; //余额
        boolean flag = true;//标记法
        for(; flag ;){
            System.out.println("=========ATM========");
            System.out.println("\t\t1.存款");
            System.out.println("\t\t2.取款");
            System.out.println("\t\t3.查询余额");
            System.out.println("\t\t4.退出");
            System.out.print("请选择：");
            int select = input.nextInt();

            switch (select){
                case 1 ->{
                    System.out.print("请输入存款金额：");
                    double money = input.nextDouble();
                    balance += money;
                }
                case 2 -> {
                    System.out.print("请输入取款金额：");
                    double money = input.nextDouble();
                    balance -= money;
                }
                case 3 -> System.out.println("余额：" + balance);
                case 4 -> flag = false;
                default -> System.out.println("输入有误！");
            }

        }
        input.close();
    }
}
