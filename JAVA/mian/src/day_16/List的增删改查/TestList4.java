package day_16.List的增删改查;

import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class TestList4 { //List集合的查操作演示
    @Test
    public void test1(){
        ArrayList<String> arrayList1 = new ArrayList<>();
        arrayList1.add("hello");
        arrayList1.add("world");
        arrayList1.add("java");
        arrayList1.add("javaA");
        arrayList1.add("javaQ");
        System.out.println(arrayList1);

        String a = arrayList1.get(1);
        System.out.println(a);
        //String b = arrayList1.getFirst();
        //System.out.println(b);
        List<String> sub  = arrayList1.subList(1,3);
        System.out.println(sub);
    }
}
