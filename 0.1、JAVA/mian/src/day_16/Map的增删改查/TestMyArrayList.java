package day_16.Map的增删改查;

import org.junit.Test;

public class TestMyArrayList {
    @Test
    public void test1(){
        MyArrayList<String> list = new MyArrayList<>();
        list.add("hello");
        list.add("world");
        list.add(0,"java");
        System.out.println(list);

        System.out.println(list.indexOf(new String("hello")));
    }

    @Test
    public void test2(){
        MyArrayList<String> list = new MyArrayList<>();
        list.add("hello");
        list.add("world");
        list.add(null);
        list.add("chai");

        System.out.println(list.indexOf("chai"));
        System.out.println(list.indexOf(null));
    }

    @Test
    public void test3(){
        MyArrayList<String> list = new MyArrayList<>();
        list.add("hello");
        list.add("world");
        list.add(null);
        list.add("chai");

        list.remove(1);
        list.remove("chai");
        System.out.println(list);
    }
}
