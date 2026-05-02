package day_14.StringJoiner;

import org.junit.Test;

import java.util.StringJoiner;

public class TestStringJoiner {
    @Test
    public void test1(){
        //拼接 hello,world,java这些单词为一个字符串，拼接时想要指定前缀，后缀，中间的连接符
        StringJoiner joiner  =new StringJoiner("-","[","]");
        joiner.add("hello");
        joiner.add("world");
        joiner.add("java");
        String str = joiner.toString();
        System.out.println(str);//[hello-world-java]
    }

    @Test
    public void test2(){
        //拼接 hello,world,java这些单词为一个字符串，拼接时想要指定前缀，后缀，中间的连接符
        StringJoiner joiner  =new StringJoiner(",");
        joiner.add("hello");
        joiner.add("world");
        joiner.add("java");
        String str = joiner.toString();
        System.out.println(str);//hello,world,java
    }
}
