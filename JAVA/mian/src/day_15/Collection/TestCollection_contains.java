package day_15.Collection;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collection;

public class TestCollection_contains {
    @Test
    public void test1(){
        Collection list = new ArrayList();
        list.add("hello");//添加元素到集合容器中
        list.add("world");
        list.add("atguigu");
        list.add("java");
        list.add("world");

        System.out.println(list.contains("world"));//true
        System.out.println(list.contains("a"));//false
        /*
        这里的contains不是String类的contains方法，而是集合的contains方法
         */
    }

    @Test
    public void test2(){
        Collection list = new ArrayList();
        list.add("hello");//添加元素到集合容器中
        list.add("world");
        list.add("atguigu");
        list.add("java");
        list.add("world");

        Collection list2 = new ArrayList();
        list2.add("java");//添加元素到集合容器中
        list2.add("hello");
        list2.add("world");

        Collection list3 = new ArrayList();
        list3.add("chai");//添加元素到集合容器中
        list3.add("hello");
        list3.add("world");


        System.out.println(list.containsAll(list2));//true
        System.out.println(list.containsAll(list3));//false
        //判断list2或list3是不是list集合的子集
    }

    @Test
    public void test3(){
        Collection list = new ArrayList();
        list.add("hello");//添加元素到集合容器中
        list.add("world");
        list.add("atguigu");
        list.add("java");
        list.add("world");

        System.out.println("元素的个数：" + list.size());//字符串的长度是用length，集合的元素个数用size方法
        System.out.println("集合为空吗？" + list.isEmpty());
    }
}
