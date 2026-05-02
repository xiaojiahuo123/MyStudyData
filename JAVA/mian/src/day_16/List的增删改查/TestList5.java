package day_16.List的增删改查;

import org.junit.Test;

import java.util.ArrayList;

public class TestList5 {//这里是关于集合的循环，增强for循环和for循环
    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        list.add("hello");
        list.add("world");
        list.add("java");
        list.add("javaA");
        list.add("javaQ");
        System.out.println(list);
        //增强for循环
        for(Object o:list){
            System.out.println(o);
        }
        //for循环
        for(int i=0;i<list.size();i++){
            System.out.println(list.get(i));
        }
    }
}
