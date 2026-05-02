package day_17.ListIterator;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.ListIterator;

public class MyListIterator {
    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world");

        //演示从头到尾遍历
        ListIterator<String> listIterator = list.listIterator();
        while(listIterator.hasNext()){
            String s = listIterator.next();
            System.out.println(s);
        }
    }

    @Test
    public void test2(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world");

        //演示从尾到头遍历
        ListIterator<String> listIterator = list.listIterator(list.size());
/*  此处是因为ArrayList集合中的size方法返回一个int数据，比如此处的数据长度是3，所以对于listIterator(int index) 方法来说，传入的索引是最后一位，从后开始向前迭代
public int size() {
    return size;
}*/
        //迭代器一开始 [size]位置，第一次previous()取[size-1]位置的元素
        while(listIterator.hasPrevious()){//判断前面还有没有元素可迭代器
            String s = listIterator.previous();//previous取迭代器当前位置的前一个位置的元素
            System.out.println(s);
        }
    }
    @Test
    public void test3(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world");

        //演示从头到尾遍历，取下标
        ListIterator<String> listIterator = list.listIterator();
        while(listIterator.hasNext()){
            int index1 = listIterator.nextIndex();
            String s = listIterator.next();
            int index2 = listIterator.nextIndex();
            System.out.println("next()方法之前：index1 = " + index1);
            System.out.println(s);
            System.out.println("next()方法之后：index2 = " + index2);
            System.out.println();
        }
    }

    @Test
    public void test4(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world");

        //演示从尾到头遍历
        ListIterator<String> listIterator = list.listIterator(list.size());
        //迭代器一开始 [size]位置，第一次previous()取[size-1]位置的元素
        while(listIterator.hasPrevious()){//判断前面还有没有元素可迭代器
            //查看接口的实现类重写接口方法previousIndex的源码，按快捷键Ctrl + Alt + B，然后选择接口的实现类
            int index1 = listIterator.previousIndex(); //previousIndex返回的是当前迭代器位置-1
            String s = listIterator.previous();//previous取迭代器当前位置的前一个位置的元素
            int index2 = listIterator.previousIndex();
            System.out.println("previous()方法之前：index1 = " + index1);
            System.out.println(s);
            System.out.println("previous()方法之后：index2 = " + index2);
            System.out.println();
        }

    }

    @Test
    public void test5(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //在所有包含"a"字母的单词后面添加一个“尚硅谷”
        //演示从头到尾遍历
        ListIterator<String> listIterator = list.listIterator();
        while(listIterator.hasNext()){
            String s = listIterator.next();
            if(s.contains("a")){//这里contains是String类的方法
                listIterator.add("尚硅谷");//迭代器的add方法，不是集合的add方法
            }
        }

        //再次查看结果
        System.out.println(list);//[hello, java, 尚硅谷, world, chai, 尚硅谷]
    }


    @Test
    public void test6(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //在所有包含"a"字母的单词后面添加一个“尚硅谷”
        //演示从尾到头遍历
        ListIterator<String> listIterator = list.listIterator(list.size());
        //迭代器一开始 [size]位置，第一次previous()取[size-1]位置的元素
        while(listIterator.hasPrevious()){//判断前面还有没有元素可迭代器
            String s = listIterator.previous();//previous取迭代器当前位置的前一个位置的元素
            if(s.contains("a")){
                listIterator.add("尚硅谷");//迭代器的add方法，不是集合的add方法
            }
        }

        //再次查看结果
        System.out.println(list);//[hello, 尚硅谷, java, world, 尚硅谷, chai]
    }

    @Test
    public void test7(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //把所有包含"a"字母的单词改为大写
        //演示从头到尾遍历
        ListIterator<String> listIterator = list.listIterator();
        while(listIterator.hasNext()){
            String s = listIterator.next();
            if(s.contains("a")){//这里contains是String类的方法
                listIterator.set(s.toUpperCase());//迭代器的set方法，不是集合的set方法
            }
        }

        //再次查看结果
        System.out.println(list);//[hello, JAVA, world, CHAI]
    }

    @Test
    public void test8(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "hello","java","world","chai");

        //删除所有包含"a"字母的单词
        //演示从头到尾遍历
        ListIterator<String> listIterator = list.listIterator();
        while(listIterator.hasNext()){
            String s = listIterator.next();
            if(s.contains("a")){//这里contains是String类的方法
                listIterator.remove();//迭代器的remove方法，不是集合的remove方法
            }
        }

        //再次查看结果
        System.out.println(list);//[hello, world]
    }
}
