package day_15.泛型.泛型方法;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collection;

public class TestWild3 {
    /*
   定义一个方法，这个方法的作用是用于遍历一个Collection系列的集合。
   遍历的效果是：
       第1个元素：xxx
       第2个元素：xxx
       第3个元素：xxx

   要求，集合的元素类型必须指定为Number或Number的父类。

此时<? super Number>可能是<Number>，<Object>
它们必须Number类或Number的父类
*/
    public void print(Collection<? super Number> coll){
        int count = 0;
        for (Object object : coll) {//增强for循环，或foreach循环。
            count++;
            System.out.println("第" + count +"个元素：" + object);
        }
    }
    @Test
    public void test1(){
        //第一个集合
        ArrayList<String> list = new ArrayList<>();
        list.add("hello");
        list.add("world");
        list.add("java");

//        print(list);//因为String不是Number的父类
    }

    @Test
    public void test2(){
        //第二个集合
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);

//        print(list);//Integer也不是Number的父类
    }

    @Test
    public void test3(){
        //第三个集合
        ArrayList<Double> list = new ArrayList<>();
        list.add(10.0);
        list.add(20.0);
        list.add(30.0);

//        print(list);//Double也不是Number的父类
    }

    @Test
    public void test4(){
        //第三个集合
        ArrayList<Object> list = new ArrayList<>();
        list.add(10.0);
        list.add(20.0);
        list.add(30.0);

        print(list);//Object是Number的父类
    }
}
