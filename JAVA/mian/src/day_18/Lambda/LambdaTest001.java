package day_18.Lambda;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class LambdaTest001 {
    @Test
    public void test(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");
        System.out.println("排序之前：" + list);

        //按照字符串的长短进行排序，从短到长
        Comparator<String> c = new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
//                return o1.length() - o2.length();
                return Integer.compare(o1.length(), o2.length());
            }
        };

        list.sort(c);
        System.out.println("排序之后：" + list);
    }

    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");
        System.out.println("排序之前：" + list);

        Comparator<String> c =  (o1, o2) -> Integer.compare(o1.length(), o2.length());
/*        public static int compare(int x, int y) {
    return (x < y) ? -1 : ((x == y) ? 0 : 1);
}*/
        //Comparator(E e1,E e2) 设计直接就是，e1和e2比较，如e1小于e2，则返回负数，e1排在e2前面，0位置不懂，正数则e1排在e2后面
        list.sort(c);
        System.out.println("排序后 ：" + list);
    }
}
