package day_16.Map的增删改查;

import org.junit.Test;

import java.util.HashMap;

public class TestMap2 {
    @Test
    public void test1(){
        HashMap<String,String> map1 = new HashMap<>();
        map1.put("张三","12");
        map1.put("张三s","112");
        System.out.println(map1);
        map1.remove("张三");
        System.out.println("rempve之后"+map1);
    }
    @Test
    public void test2(){
        HashMap<String,String> map1 = new HashMap<>();
        map1.put("张三","12");
        map1.put("张三s","112");
        System.out.println(map1);
        map1.remove("张三s","112");
        System.out.println(map1);
    }

    @Test
    public void test3(){
        HashMap<String,String> map1 = new HashMap<>();
        map1.put("张三","12");
        map1.put("张三s","112");
        System.out.println(map1);
        boolean Flag = map1.isEmpty();
        System.out.println(Flag);
        System.out.println(map1.size());
        map1.clear();
        System.out.println(map1);
    }
}
