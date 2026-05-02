package day_16.Map的增删改查;

import org.junit.Test;

public class MyArrayListTestClass {
    @Test
    public void test(){
        MyArrayListTest<String> myArrayListTest= new MyArrayListTest<>();

        myArrayListTest.add("sasas");
        myArrayListTest.add("极大·1");
        myArrayListTest.add(0,"fdfe");
        System.out.println(myArrayListTest);

        System.out.println(myArrayListTest.chaxun("sasas"));

        myArrayListTest.remove(0);
        System.out.println("使用remove(int index)后 :"+myArrayListTest);
    }
}
