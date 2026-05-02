package day_16;

import org.junit.Test;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Random;

public class TestMapImpl {//
    @Test
    public void test1(){
        long start = System.currentTimeMillis();
        ArrayList<Integer> list = new ArrayList<>();
        list.add(Integer.valueOf(1));//这里先添加1个，保证list.size()不为0
        Random random = new Random();
        for(int i=1; i<=10000; i++){
            int index = random.nextInt(0, list.size());
            list.add(index, i);
        }
        long end = System.currentTimeMillis();
        System.out.println("时间：" + (end-start));//时间：4
    }

    @Test
    public void test2(){
        long start = System.currentTimeMillis();
        LinkedList<Integer> list = new LinkedList<>();
        list.add(Integer.valueOf(1));//这里先添加1个，保证list.size()不为0
        Random random = new Random();
        for(int i=1; i<=10000; i++){
            int index = random.nextInt(0, list.size());
            list.add(index, i);
        }
        long end = System.currentTimeMillis();
        System.out.println("时间：" + (end-start));//时间：68
    }
}
