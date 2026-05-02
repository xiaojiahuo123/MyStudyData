package day_14.math;

import org.junit.Test;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;

public class TestBig {
    @Test
    public void test1(){
//        long a = 863214563214563214589321456325632521452L;//超出long范围
        BigInteger a = new BigInteger("863214563214563214589321456325632521452");
        BigInteger b = new BigInteger("896954562145215245244253215323296214586214521452");

        //凡是对象要完成xx功能，就是通过调用方法
        System.out.println("和：" + a.add(b));
        System.out.println("差：" + a.subtract(b));
        System.out.println("乘积：" + a.multiply(b));
        System.out.println("商：" + a.divide(b));
        System.out.println("余数：" + a.remainder(b));
    }

    @Test
    public void test2(){
        double d = 896954562145215245244253215323296214586214521452.0;
        System.out.println(d);
    }

    @Test
    public void test3(){
        BigDecimal a = new BigDecimal("896954562145215245244253215323296214586214521452.0");
        BigDecimal b = new BigDecimal("896954562145.215245244253215323296214586214521452");
        //凡是对象要完成xx功能，就是通过调用方法
        System.out.println("和：" + a.add(b));
        System.out.println("差：" + a.subtract(b));
        System.out.println("乘积：" + a.multiply(b));
        System.out.println("商：" + a.divide(b));
        System.out.println("余数：" + a.remainder(b));

    }

    @Test
    public void test4(){
        BigDecimal a = new BigDecimal("896954562145215245244253215323296214586214521452.0");
        BigDecimal b = new BigDecimal("86214522.395251");
        //凡是对象要完成xx功能，就是通过调用方法
        System.out.println("和：" + a.add(b));
        System.out.println("差：" + a.subtract(b));
        System.out.println("乘积：" + a.multiply(b));
//        System.out.println("商：" + a.divide(b));//除不尽
        System.out.println("商：" + a.divide(b,1000, RoundingMode.CEILING));
        //这里的1000代表保留到小数点后1000位
        //这里的RoundingMode.CEILING代表第1001位的怎么处理，CEILING代表进位
        System.out.println("余数：" + a.remainder(b));

    }
}
