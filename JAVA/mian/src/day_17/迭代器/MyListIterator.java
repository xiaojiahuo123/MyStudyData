package day_17.迭代器;

import day_17.MyLinkedList.MyLinkedList;
import org.junit.Test;

import java.util.Iterator;

public class MyListIterator {
    @Test
    public  void test(){
        MyLinkedList_Iterator<String> Mynew = new MyLinkedList_Iterator<>();
        Mynew.add("1");
        Mynew.add("2");
        Mynew.add("3");
        Mynew.add("4");
        Mynew.add("5");

        Iterator<String> myIterable =  Mynew.iterator();
        for(String str : Mynew){
            System.out.println(str);
        }
    }
}
