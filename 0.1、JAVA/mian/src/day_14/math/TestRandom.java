package day_14.math;

import org.junit.Test;

import java.util.Random;

public class TestRandom {
    @Test
    public void test1(){
        double d = Math.random();//[0,1)
        //[a,b)范围的整数
        int a = 10;
        int b = 50;
        int num = (int) (Math.random() * (b - a) + a);
        System.out.println("num = " + num);
    }

    @Test
    public void test2(){
        Random r = new Random();
        double a = r.nextDouble();
        boolean b = r.nextBoolean();
        int c = r.nextInt();//int范围的任意整数
        int d = r.nextInt(100);//[0,100)
        int e = r.nextInt(10,50);//[10,50)  这个方法的版本比较新

        System.out.println("a = " + a);// 0.9671156811567097
        System.out.println("b = " + b);//true
        System.out.println("c = " + c);//-327530929
        System.out.println("d = " + d);//52
        System.out.println("e = " + e);//48
    }
}
