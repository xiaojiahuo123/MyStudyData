package day_18.Lambda;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.function.Consumer;

public class LambdaTest002 { //c
    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //遍历上述集合，查看每一个单词的长度
        //(1)foreach循环（复习）
        for (String s : list) {
            System.out.println(s +"的长度：" + s.length());
        }
    }

    @Test
    public void test2(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //遍历上述集合，查看每一个单词的长度
        //(2)迭代器Iterator（复习）
        Iterator<String> iterator = list.iterator();
        while(iterator.hasNext()){
            String s = iterator.next();
            System.out.println(s +"的长度：" + s.length());
        }
    }

    @Test
    public void test3(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //遍历上述集合，查看每一个单词的长度
        //(3)forEach方法
        Consumer<String> c = new Consumer<String>() {
            @Override
            public void accept(String s) {
                System.out.println(s +"的长度：" + s.length());
            }
        };//匿名内部类写法
        list.forEach(c);
    }

    @Test
    public void test4(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //遍历上述集合，查看每一个单词的长度
        //(3)forEach方法
//        Consumer<String> c = (String s) ->{System.out.println(s +"的长度：" + s.length());};//Lambda表达式原型
       /* Consumer<String> c = s ->System.out.println(s +"的长度：" + s.length());//Lambda表达式简化
        list.forEach(c);*/

        list.forEach(s ->System.out.println(s +"的长度：" + s.length()));
    }
}
