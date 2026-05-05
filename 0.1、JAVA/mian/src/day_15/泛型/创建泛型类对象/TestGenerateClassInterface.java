package day_15.泛型.创建泛型类对象;

import org.junit.Test;

import java.util.ArrayList;
import java.util.HashSet;

public class TestGenerateClassInterface {
    @Test
    public void test1(){
        //对于集合来说，<>里面应该填写集合元素的具体类型
        //从JDK7开始，右边<>中的类型可以省略，它可以根据左边<>中的类型自动推断，但是<>得保留
        //如果<>省略的话，会有警告，因为它认为你擦除了泛型
        ArrayList<String> list = new ArrayList<>();//表示它的元素只能是String及其子类
        list.add("hello");
        list.add("world");
        System.out.println(list);

        ArrayList<Integer> list2 =new ArrayList<>();//表示它的元素只能是Integer及其子类
        list2.add(1);
        list2.add(2);
        System.out.println(list2);

        HashSet<Student> set = new HashSet<>();//表示它的元素只能是Student及其子类
//        set.add("张三"); //"张三"表示字符串类型
        set.add(new Student(2,"张三",23));
        System.out.println(set);
    }
}
