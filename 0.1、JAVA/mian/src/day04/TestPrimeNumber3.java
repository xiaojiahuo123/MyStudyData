package day04;

import java.util.Scanner;

public class TestPrimeNumber3 {
    public static void main(String[] args) {
        //从控制台接收一个整数，判断它是不是素数
        //什么是素数？也叫质数，它是大于1的自然数，并且只能被1和他本身整数
        //例如：7是素数
        Scanner input = new Scanner(System.in);

        System.out.print("请输入一个整数：");
        int num = input.nextInt();

        /*
        假设num是17
            [2,16]全部都找完，发现没有17的约数，再下结论说，17是素数
            [2,17的平方根]范围内，找17的约数即可，找到就找到了，找不到肯定没有了，
            因为  num = a * b，  a是小的约数，b是大的约数， 最极端的情况a=b，a是num的平方根

        假设num是20
            2,4,5,10

            Math.sqrt(num)表示求num的平方根
         */
        int i;
        for(i=2; i<=Math.sqrt(num); i++) {
            if(num%i==0){//i是num的约数
                break;
            }
        }
        if (i==num) {
            System.out.println(num + "是素数");
        } else {
            System.out.println(num + "不是素数");
        }

        input.close();
    }
}
