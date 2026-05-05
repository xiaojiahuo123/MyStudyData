package day_13.test_01异常.MyJUnit;

import java.util.Scanner;

public class MyTest {
    // 用于处理键盘输入的方法
    public int calculateSumFromInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入第一个整数：");
        int num1 = scanner.nextInt();
        System.out.println("请输入第二个整数：");
        int num2 = scanner.nextInt();
        scanner.close();
        return num1 + num2;
    }
    
    // 用于验证输入是否为正数的方法
    public boolean isPositiveNumber() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入一个数字：");
        int number = scanner.nextInt();
        scanner.close();
        return number > 0;
    }
    
    // 用于测试的辅助方法，接受Scanner作为参数以便测试
    public int calculateSum(Scanner scanner) {
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        return num1 + num2;
    }
    
    // 用于测试的辅助方法，接受Scanner作为参数以便测试
    public boolean checkPositive(Scanner scanner) {
        int number = scanner.nextInt();
        return number > 0;
    }
}
