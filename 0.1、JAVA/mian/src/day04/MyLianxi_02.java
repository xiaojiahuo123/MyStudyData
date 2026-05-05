package day04;

import java.util.Scanner;

public class MyLianxi_02 {
    public static void main(String[] args) {
        // 创建Scanner对象用于读取控制台输入
        Scanner scanner = new Scanner(System.in);

        System.out.print("请输入一个整数：");
        int number = scanner.nextInt();

        // 判断是否为素数
        boolean isPrime = isPrimeNumber(number);

        // 输出结果
        if (isPrime) {
            System.out.println(number + " 是素数");
        } else {
            System.out.println(number + " 不是素数");
        }

        // 关闭Scanner
        scanner.close();
    }

    /**
     * 判断一个数是否为素数
     * 素数是大于1的自然数，且只能被1和自身整除
     */
    public static boolean isPrimeNumber(int num) {
        // 小于等于1的数不是素数
        if (num <= 1) {
            return false;
        }

        // 2是最小的素数
        if (num == 2) {
            return true;
        }

        // 偶数不是素数（除了2）
        if (num % 2 == 0) {
            return false;
        }

        // 检查从3到sqrt(num)的奇数是否能整除num
        // 只需检查到平方根，因为如果n有一个大于其平方根的因子，
        // 那么它必定有一个小于其平方根的对应因子
        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }
}
