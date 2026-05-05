package day_15.Set;

import org.junit.Test;

import java.util.*;

public class TestSet {
    @Test
    public void test1(){
        HashSet set = new HashSet();
        //Set接口的方法与Collection接口的一样

        set.add("hello");
        set.add("world");
        set.add("java");
        set.add("java");
        set.add("java");

        System.out.println(set);
        //[world, java, hello]
        //无规律
    }

    @Test
    public void test2(){
        Collection list = new ArrayList();
        list.add("hello");
        list.add("world");
        list.add("java");
        list.add("java");
        list.add("java");

        System.out.println(list);
        //[hello, world, java, java, java]
        //list集合元素可重复，有顺序
    }

    @Test
    public void test3(){
        LinkedHashSet set = new LinkedHashSet();
        //Set接口的方法与Collection接口的一样

        set.add("hello");
        set.add("world");
        set.add("java");
        set.add("java");
        set.add("java");

        System.out.println(set);
        //[hello, world, java]
        //按照元素的添加顺序排列
    }

    @Test
    public void test4(){
        TreeSet set = new TreeSet();
        //Set接口的方法与Collection接口的一样

        set.add("hello");
        set.add("world");
        set.add("java");
        set.add("java");
        set.add("java");
        System.out.println(set);
        //[hello, java, world]
        //按照元素的大小顺序排列
        //因为元素是String类型，所以会用到String类的compareTo方法比较两个字符串的大小
        //String类中compareTo方法是按照字符的Unicode编码值来比较
    }

    @Test
    public void test5(){
        TreeSet set = new TreeSet();

        set.add(new Student(2,"张三",89));
        set.add(new Student(1,"李四",100));
        set.add(new Student(3,"王五",96));

        System.out.println(set);
        //按照元素的大小顺序排列
        //因为元素是Student类型，所以会用到Student类的compareTo方法比较两个学生对象的大小
        //要求Student必须实现Comparable接口
    }

    @Test
    public void test6(){
        //想要元素按照长短顺序排列，需要定制比较器
        //定义匿名内部类，实现Comparator接口，重写int compare(Object o1, Object o2)方法
        Comparator c = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                String s1 = (String) o1;
                String s2 = (String) o2;
                return s1.length() - s2.length();
            }
        };

        TreeSet set = new TreeSet(c);//一会儿添加元素时，调用c的compare方法来比较元素的大小，决定它的存储位置
        //Set接口的方法与Collection接口的一样

        set.add("hello");
        set.add("world");
        set.add("java");
        set.add("java");
        set.add("java");
        System.out.println(set);
        //[java, hello]
    }

    @Test
    public void test7(){
        //想要元素按照长短顺序排列，需要定制比较器
        //定义匿名内部类，实现Comparator接口，重写int compare(Object o1, Object o2)方法
        //如果长度相同，再看编码值
        Comparator c = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                String s1 = (String) o1;
                String s2 = (String) o2;
                int result = s1.length() - s2.length();
                return result != 0 ? result : s1.compareTo(s2);
            }
        };

        TreeSet set = new TreeSet(c);//一会儿添加元素时，调用c的compare方法来比较元素的大小，决定它的存储位置
        //Set接口的方法与Collection接口的一样

        set.add("hello");
        set.add("world");
        set.add("java");
        set.add("java");
        set.add("java");
        System.out.println(set);
        //[java, hello, world]
    }

    @Test
    public void test88(){
        HashSet set = new HashSet();
        set.add(new Employee(1,"张三"));
        set.add(new Employee(1,"张三"));

        System.out.println(set);
        //[Employee{id=1, name='张三'}, Employee{id=1, name='张三'}]
        //重写equals和hashCode方法，就可以去重
    }
}
