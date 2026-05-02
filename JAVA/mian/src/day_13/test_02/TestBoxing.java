package day_13.test_02;

import org.junit.Test;

public class TestBoxing {
    @Test
    public void test1(){
        Integer i = 1;//自动装箱，左边是引用数据类型，右边是基本数据类型
        int j = i;//自动拆箱，i是对象，j是基本数据类型
    }

    @Test
    public void test2(){
        Integer i = 200;
        int j = 200;
        System.out.println(i == j);//把i自动拆箱，变为2个int值比较
    }

    @Test
    public void test3(){
        Integer i = 200;
        Integer j = 200;
        System.out.println(i == j);//false  比较两个对象的地址值
    }

    @Test
    public void test4(){
        Integer i = 200;
        Double j = 200.0;
        //System.out.println(i == j);//报错， 两个对象的类型不一致，它们之间也没有父子类关系，是无法比较地址是否相等

    }

    @Test
    public void test5(){
        Integer i = 200;
        double j = 200.0;
        System.out.println(i == j);//i会自动拆箱
    }

    @Test
    public void test6(){
        Integer i = 200;
        Double j = 200.0;
        System.out.println(i > j);//两个都拆箱会基本数据类型
    }

    @Test
    public void test7(){
        // Double d = 1; //无法自动装箱
        // int a = d;//无法自动拆箱
        //Double 对应的类型 double
        //int 对应的类型是Integer
        //int 与 Double不是对应类型

        double d = 1;//基本数据类型的自动提升
        Double d2 = 1.0;
        Double d3 = 1D; //D代表double类型
    }
}
