package day_16.List的增删改查;

import org.junit.Test;

import java.util.ArrayList;
import java.util.function.UnaryOperator;

public class TestList3 {
    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        list.add("a");
        list.add("b");
        list.add("c");
        //list.set(1,"世界");//set()方法是直接将对应下标的元素改为所需的内容
        System.out.println(list.set(1,"世界"));//返回值是下标位置的原本元素
        System.out.println(list);
    }

/*
replaceAll方法的形参是UnaryOperator<T>类型的接口，
它又继承了Function<T, R>接口，它的抽象方法  R apply(T t);
在UnaryOperator<T>接口中的 抽象方法  T apply(T t)
现在是在集合的replaceAll方法这个上下文中，那么它是要完成把旧元素替换为新元素。
参数代表旧元素，返回值代表新元素，类型相同，可能值不同了

需求：把test2(){}中list的元素单词的首字母改为大写
*/
    @Test
    public void test2(){
        ArrayList<String> list = new ArrayList<>();
        list.add("hello");
        list.add("world");
        list.add("java");

        UnaryOperator<String> u = new UnaryOperator<String>() {
            @Override
            public String apply(String s) {//s代表list集合的旧元素，apply方法的返回值代表list集合的新元素
                //把s中的单词首字母改为大写
                //思路：截取首字母，把首字母改为大写，再与剩下的字母拼接起来
                /*String first = s.substring(0,1);
                first = first.toUpperCase();
                String after = s.substring(1);
                return first + after;*/

                return s.substring(0,1).toUpperCase().concat(s.substring(1));
/*实现逻辑：
- s.substring(0,1) ：截取字符串的第一个字符
- .toUpperCase() ：将第一个字符转换为大写
- .concat(s.substring(1)) ：将大写首字母与剩余部分拼接

- replaceAll 是 List 接口的方法，用于 批量替换集合中的所有元素
- 参数为 UnaryOperator<E> 类型，即转换规则
- 执行后，原集合中的每个元素都会被 apply 方法的返回值替换
*/
            }
        };
        list.replaceAll(u);//上述的apply方法在replaceAll方法内部调用
        System.out.println(list);//[Hello, World, Java]
    }
}
