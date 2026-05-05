package day_13.test_01异常.MyJUnit;

import org.junit.Test;

import java.util.Scanner;

public class TestJUnit {
    @Test
    public void test1(){
        System.out.println("hello");
    }

    @Test
    public void test2(){
        System.out.println("hello2");
    }

    @Test
    public void test3(){
        Scanner input = new Scanner(System.in);

        System.out.print("请输入一个整数：");
        int num = input.nextInt();
        System.out.println("num = " + num);

        input.close();
    }
}
