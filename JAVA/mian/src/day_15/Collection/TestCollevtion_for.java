package day_15.Collection;

import java.util.ArrayList;
import java.util.Collection;

//Collevtion集合的遍历
public class TestCollevtion_for {
    public static void main(String[] args) {
        Collection list1 = new ArrayList();
        list1.add("1daefd");//添加元素到集合容器中
        list1.add("2adf");
        list1.add("3htf");
        list1.add("4hgk");
        System.out.println("初始"+list1);
//如果想要队集合中的元素做某些操作，就需要循环或者使用迭代器
        for (Object o : list1) {
            String s = (String) o;
            System.out.println("长度为"+s.length()+","+s);
        }
    }
}
