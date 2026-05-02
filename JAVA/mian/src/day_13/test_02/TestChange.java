package day_13.test_02;

import org.junit.Test;

public class TestChange {
    @Test
    public void test1(){
        Integer a = 1;
        int[] nums = {1};//一个元素的数组
        int b = 1;
        change(a, nums,b );
        System.out.println("a = " + a);//a = 1
        System.out.println("nums[0] = " + nums[0]);//nums[0] = 2
        System.out.println("b = " + b);//b=1
    }

    public void change(Integer i,int[] arr, int k){
        //因为包装类对象不可变，那么只要修改包装类对象的值，就会得到新对象
        i++; //等价于 i = new Integer(i+1);
        System.out.println(i == i - 1 ? "true" : "false");
        System.out.println(i);
        System.out.println(i-1);
        i=10; //等价于 i = new Integer(10);

        arr[0]++;
        arr = new int[2];//一旦形参指向新对象，就与原来实参对象无关了
        arr[0] = 10;

        k++; //形参是基本数据类型，无论怎么修改都与实参无关
    }
}
