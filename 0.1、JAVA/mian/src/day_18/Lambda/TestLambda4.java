package day_18.Lambda;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.function.UnaryOperator;

public class TestLambda4 {

    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //要将上述单词转为大写
        UnaryOperator<String> u = new UnaryOperator<String>() {
            @Override
            public String apply(String s) {
                return s.toUpperCase();
            }
        };//匿名内部类写法
        list.replaceAll(u);
    }

    @Test
    public void test2(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //要将上述单词转为大写
//        UnaryOperator<String> u = (String s)-> {return s.toUpperCase();};//Lambda表达式原型
      /*  UnaryOperator<String> u = s-> s.toUpperCase();//Lambda表达式简化
        list.replaceAll(u);*/

        list.replaceAll(s-> s.toUpperCase());
        System.out.println(list);
    }
}
