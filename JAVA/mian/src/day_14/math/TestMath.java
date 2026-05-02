package day_14.math;

import org.junit.Test;

public class TestMath {
    @Test
    public void test(){
        //求2的10次方
        System.out.println(Math.pow(2,10));//1024.0

        //求近似整数值
        System.out.println(Math.round(2.7));//3  类似于四舍五入
        System.out.println(Math.ceil(2.7));//3.0  向上取整
        System.out.println(Math.floor(2.7));//2.0 向下取整

        System.out.println(Math.round(2.3));//2
        System.out.println(Math.ceil(2.3));//3.0
        System.out.println(Math.floor(2.3));//2.0

        System.out.println(Math.round(2.5));//3
        System.out.println(Math.round(-2.5));//-2
        System.out.println(Math.round(-2.6));//-3
        System.out.println(Math.round(-2.4));//-2
        // Math.round(x)   (int)(x + 0.5)
        //2.5 + 0.5 = (int)3.0 = 3
        //-2.5 + 0.5 = (int)-2.0 = -2
        //-2.6 + 0.5 = (int)-2.1 = -3  向下取整 往小
        //-2.4 + 0.5 = (int)-1.9 = -2  向下取整 往小
    }

    @Test
    public void test2(){
        int x = 3;
        int y = 2;

        System.out.println(Math.max(x,y));//3
        System.out.println(Math.min(x,y));//2
    }
}
