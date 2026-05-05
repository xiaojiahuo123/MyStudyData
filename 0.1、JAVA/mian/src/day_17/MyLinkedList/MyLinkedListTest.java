package day_17.MyLinkedList;

import org.junit.Test;

public class MyLinkedListTest {
    @Test
    public void test1(){
        MyLinkedList<String> list = new MyLinkedList<>();
        list.add("hello");
        list.add("world");
        list.add("java");
        list.add("atguigu");
        list.add("chai");
        System.out.println(list);

        list.remove("java");
        System.out.println(list);

        list.remove("hello");
        System.out.println(list);

        list.remove("chai");
        System.out.println(list);

        list.remove("world");
        System.out.println(list);

        list.remove("atguigu");
        System.out.println(list);
    }
}
