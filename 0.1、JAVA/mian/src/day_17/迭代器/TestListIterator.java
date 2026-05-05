package day_17.迭代器;

import org.junit.Test;

import java.util.ArrayList;
import java.util.ListIterator;

public class TestListIterator {
    @Test
    public void test1() {
        ArrayList<String> list = new ArrayList<>();
        list.add("1");
        list.add("2");
        list.add("3");
        list.add("4");

        //此处的也是一样的，通过这个方法创建迭代器内部类的实例对象，返回这个实例对象，listiterator接收
        ListIterator<String> listiterator = list.listIterator();
       while (listiterator.hasNext()) {
           String next = listiterator.next();
           System.out.println(next);
       }
    }
}
