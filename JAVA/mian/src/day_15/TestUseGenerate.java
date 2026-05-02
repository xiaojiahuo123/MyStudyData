package day_15;

import org.junit.Test;

import java.util.ArrayList;

public class TestUseGenerate {
    @Test
    public void test1(){
        //以下代码使用了泛型
        //往集合中添加一组字符串
        ArrayList<String> list = new ArrayList<String>();
        list.add("hello");
        list.add("world");
        //list.add(1);//1不是字符串
        //此时编译器就可以给出类型检查，1不符合字符串类型
        //可以提前避免不必要的错误。

        //查看每一个字符串的内容和长度
        for (String s : list) {
            System.out.println(s +"的长度：" + s.length());
        }
    }
}
