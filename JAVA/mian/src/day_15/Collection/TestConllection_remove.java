package day_15.Collection;

import java.util.ArrayList;
import java.util.Collection;
import java.util.function.Predicate;

public class TestConllection_remove {
    public static void main(String[] args) {
//        集合Conllection 中删除的学习
        Collection  list1 = new ArrayList();
        list1.add("1daefd");//添加元素到集合容器中
        list1.add("2adf");
        list1.add("3htf");
        list1.add("4hgk");
        System.out.println("初始"+list1);

        list1.remove("2adf");
        System.out.println("使用remove删除adf元素"+ list1);

        Collection  list2 = new ArrayList();
        list2.add("1daefd");
        list2.add("2nfghn");
        list2.add("3sdf");
        list2.add("4ghkmgu");
        list2.add("5daedrgfd");
        System.out.println("初始的list2"+ list2);
        list1.removeAll(list2);
        System.out.println("使用removeAll方法后"+list1);

        Collection list3 = new ArrayList();
        list3.addAll(list1);
        System.out.println("清空前list3"+list3);
        list3.clear();
        System.out.println("清空后List3"+list3);
/*
removeIf方法是JDK8引入的，
这个方法的形参是Predicate接口类型
调用这个方法时，需要传入一个Predicate接口的实现类的对象。
需要用有名字的类或匿名内部类实现Predicate接口，重写public boolean test(Object obj)方法
这个方法中，用于编写删除元素的条件。此时方法的形参obj就是代表集合中的元素，
元素满足某个删除条件，就返回true，否则返回false
 */
        Predicate p = new Predicate(){
            public boolean test(Object o) {
                String str = (String) o;
                return str.contains("a");
            }
        };
        list1.removeIf(p);
/*
在集合的removeIf方法的内部，会遍历集合的元素，然后每一个元素都会调用p的test方法进行判断，看它是否满足删除条件。
*/
        System.out.println("调用removeIf方法后的list1"+list1);
    }
}
