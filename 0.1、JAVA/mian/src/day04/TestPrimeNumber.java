package day04;

import java.util.Scanner;

public class TestPrimeNumber {
    public static void main(String[] args) {
        //从控制台接收一个整数，判断它是不是素数
        //什么是素数？也叫质数，它是大于1的自然数，并且只能被1和他本身整数
        //例如：7是素数
        Scanner input = new Scanner(System.in);

        System.out.print("请输入一个整数：");
        int num = input.nextInt();

        //思考：怎么在[2,num-1]范围内找num的约数，
        // 如果找到1个约数，num就不是素数
        /*for(int i=2; i<num; i++) {
            if (num%i==0) {//i是num的约数
                System.out.println(num + "不是素数");
                break;
            } else {
                System.out.println(num + "是素数");
            }
        }*/
        /*
        上面的代码是错误的，原因是：
            在[2, num-1]范围内找到任意1个num的约数，确实可以断定num不是素数。
            但是不能因为某一个i不是num的约数，就说num是素数
         */
        boolean flag = true;//这里true的意思，是假设num是素数
        for(int i=2; i<num; i++) {
            if(num%i==0){//i是num的约数
                flag = false;
                break;
            }
        }
        if (flag) {
            System.out.println(num + "是素数");
        } else {
            System.out.println(num + "不是素数");
        }

        input.close();
    }
}
