package day_15.泛型.有名字的类实现泛型接口;

import java.util.TreeSet;

public class TestGenerateClassInterface {
    public void test1(){

        Rectangle rectangle = new Rectangle(2.3,4.5);
        Rectangle rectangle2 = new Rectangle(2.33,4.55);
        Rectangle rectangle3 = new Rectangle(2.34,4.5);


        //使其按照面积排序
        //默认按照Rectangle的compareTo方法比较大小，按照面积比较大小
        TreeSet<Rectangle> set = new TreeSet<>();//TreeSet本身就是有序的，而我们在Rectangle类中实现了Comparable<T>接口按照对象进行排序，
        // 所以我们直接添加后就自动排序了，不用再专门对其进行排序
        set.add(new Rectangle(5,3));
        set.add(new Rectangle(4,2));
        set.add(new Rectangle(6,1));
        System.out.println(set);
    }
}
