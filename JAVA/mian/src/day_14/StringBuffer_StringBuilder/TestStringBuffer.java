package day_14.StringBuffer_StringBuilder;

import org.junit.Test;

public class TestStringBuffer {
    @Test
    public void test1(){
        StringBuffer s = new StringBuffer();
        s.append("hello");
        s.append("world");//末尾追加
        s.append("atguigu");
        //默认扩容是 数组的长度 * 2 + 2

    }
    @Test
    public void test2(){
        StringBuffer s = new StringBuffer(0);
        //思考题：为什么有+2？
        //如果手动指定了初始容量为0，首次扩容时，也能的2的长度
    }

    @Test
    public void test3(){
        StringBuffer s = new StringBuffer();
        s.append("hello");
        s.append("world");

        s.insert(5,"chailinyan");//中间插入
        System.out.println(s);//hellochailinyanworld
    }

    @Test
    public void test4(){
        StringBuffer s = new StringBuffer();
        s.append("hello");
        s.append("world");
        System.out.println(s);//helloworld

        s.delete(3,6);//[3,6)删除多个字符
        System.out.println(s);//helorld

        s.deleteCharAt(1);//删除1个字符
        System.out.println(s);//hlorld
    }

    @Test
    public void test5(){
        StringBuffer s = new StringBuffer("helloworld");
        s.replace(3,7,"chai");//替换[3,7)范围的字符
        System.out.println(s);//helchairld
    }

    @Test
    public void test6(){
        StringBuffer s = new StringBuffer("helloworld");
        s.reverse();//反转
        System.out.println(s);//dlrowolleh
    }

    @Test
    public void test7(){
        StringBuffer s = new StringBuffer("helloworld");
        s.setCharAt(1,'a');//修改[1]位置的字符
        System.out.println(s);//halloworld
        s.setLength(5);
        System.out.println(s);//hallo
        s.setLength(10);//可以改长，但是后面是空字符
        System.out.println(s);//hallo
    }

    @Test
    public void test8(){
        StringBuffer s = new StringBuffer("helloworld");

        int index = s.indexOf("o");
        System.out.println("index = " + index);//index = 4

        int last = s.lastIndexOf("o");
        System.out.println("last = " + last);//last = 6
    }

    @Test
    public void test10(){
        StringBuffer s = new StringBuffer("helloworld");

        int length = s.length();
        System.out.println("length = " + length);//length = 10  字符的个数
    }
}
