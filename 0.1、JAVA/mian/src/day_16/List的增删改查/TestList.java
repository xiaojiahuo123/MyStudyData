package day_16.List的增删改查;

import org.junit.Test;

import java.util.ArrayList;

public class TestList {
    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        list.add("a");
        list.add("b");
        list.add("c");
        list.add("d");
        System.out.println("list内容是"+ list);
    }

    @Test
    public void test2(){
     ArrayList<String> list = new ArrayList<>();
        list.add("a");
        list.add("b");
        list.add("c");
        System.out.println(list);
        list.remove(2);
        System.out.println();
    }

    @Test
    public  void test3(){
        ArrayList<String> list = new ArrayList<>();
        list.add("hello");
        list.add("world");
        list.add("java");

        System.out.println(list.remove("hello"));//true   [world,java]
        System.out.println(list.remove(1));//java 返回被删除元素
    }
}
