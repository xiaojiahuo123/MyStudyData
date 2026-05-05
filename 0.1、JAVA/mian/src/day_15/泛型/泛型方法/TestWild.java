package day_15.泛型.泛型方法;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collection;

public class TestWild {
    /*
  定义一个方法，这个方法的作用是用于遍历一个Collection系列的集合。
  遍历的效果是：
      第1个元素：xxx
      第2个元素：xxx
      第3个元素：xxx

   此时<?>可能是<String>，<Integer>，。。。。
   */
    public void print(Collection<?> coll){
        int count = 0;
        for (Object object : coll) {//增强for循环，或foreach循环。
            count++;
            System.out.println("第" + count +"个元素：" + object);
        }
    }


/*
要求，集合的元素类型只能是Number或Number的子类。

此时<? extends Number>可能是<Double>，<Integer>，<BigDecimal>。。。。
它们必须是继承Number类
需要中注意的是，但在Java中，泛型信息只在编译时存在，在运行时会被擦除：

- Collection<?> 在类型擦除后变为 Collection<Object>
- Collection<? extends Number> 在类型擦除后变为 Collection<Number>

两个print方法无法构成重载的原因是Java泛型的类型擦除机制。
具体来说：
1. 第一个方法定义为 public void print(Collection<?> coll)
2. 第二个方法定义为 public void print(Collection<? extends Number> coll)
虽然从表面上看这两个方法的参数类型不同，但在Java中，泛型信息只在编译时存在，
然而，方法重载的判断是基于方法签名的，而方法签名只包括方法名和参数类型。由于Java的类型擦除机制，
这两个方法在编译后实际上具有相同的方法签名： print(Collection) ，因此编译器会认为这是重复定义的方法，导致编译错误。
简单的说，泛型这里的<?>和<? extends Number>在编译后都是Collection<Object>，
因此无法构成重载。
*/

    public void printlns(Collection<? extends Number> coll){
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

        print(list);
    }

    @Test
    public void test2(){
        //第二个集合
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);

        print(list);
    }
}
