package day_15.Collection;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collection;
//演示Collection接口的添加方法
public class TestCollection1 {
    @Test
    public void test1(){
        //ArrayList list  = new ArrayList();//正常来说，应该这么写
        Collection list = new ArrayList();//准备了一个容器，装对象的容器，此时没有元素
        /*
        这里这么写有两个用意：
        （1）强调以下 ArrayList 是 Collection接口的实现类，注意一下它们的关系
        （2）ArrayList类的方法比Collection接口要多，因为子类有扩展新的方法。
            现在是学习Collection接口的方法，采用多态引用的话，遵循：编译时看左边，运行时看右边。
            编译时只能看到Collection接口的方法
         */
        list.add("hello");//添加元素到集合容器中
        //list.add("world");
        list.add("world");
        list.add("java");
        list.add("atguigu");

        System.out.println(list);//自动调用list的toString方法，说明ArrayList重写了toString方法
        //可以看到元素情况
        //[hello, world, java, atguigu]
    }

    @Test
    public void test2(){
        Collection list = new ArrayList();
        list.add("hello");//添加元素到集合容器中
        list.add("world");

        Collection list2 = new ArrayList();
        list2.add("java");//添加元素到集合容器中
        list2.add("atguigu");
        list2.add("hello");

        //想要把第二个集合list2的元素，也添加到第一个集合list中
        list.addAll(list2);//list = list ∪ list2
        //数学中 集合的元素是不能重复的，此时ArrayList这个集合的元素是可以重复的
        System.out.println(list);//[hello, world, java, atguigu, hello]
    }
}
