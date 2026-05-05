package day_16;

import org.junit.Test;

import java.util.Stack;

public class TestStack {//栈学习
    @Test
    public void test1(){
        //Stack新增的方法
        Stack<String> stack = new Stack<>();
        stack.push("hello");
        stack.push("world");
        stack.push("java");
        stack.push("atguigu");

        System.out.println(stack.pop());//直接打印pop方法的返回值  atguigu
        System.out.println(stack.pop());//直接打印pop方法的返回值  java
        System.out.println(stack.pop());//直接打印pop方法的返回值  world
        System.out.println(stack.pop());//直接打印pop方法的返回值  hello
        System.out.println(stack.pop());//直接打印pop方法的返回值 报错EmptyStackException空栈异常
    }

    @Test
    public void test2(){
        //Stack新增的方法
        Stack<String> stack = new Stack<>();
        stack.push("hello");
        stack.push("world");
        stack.push("java");
        stack.push("atguigu");

        System.out.println(stack.peek());//atguigu
        System.out.println(stack.peek());//atguigu
        System.out.println(stack.peek());//atguigu

        System.out.println(stack.search("world"));//3
        System.out.println(stack.search("atguigu"));//1
    }
}
