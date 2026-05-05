package day_17.迭代器;

import org.junit.Test;

import java.util.*;

public class TestIterator {
/* boolean hasNext()：判断是否还有元素可迭代
- E next()：取出迭代器当前位置的元素，然后让迭代器走向下一个元素。*/
    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "a", "b", "c");
        Iterator<String> iterator = list.iterator();  //Conllection集合的子类ArrayList的list是可以调用iterator()方法的，得到一个名为iterator的Iterator<String>的实例化对象
        while(iterator.hasNext()){
            String s = iterator.next();
            //iterator.next();
            System.out.println(s);
        }
    }

    @Test
    public void test3(){
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1,"hello");
        map.put(2,"world");
        map.put(3,"java");

        Set<Map.Entry<Integer, String>> entries = map.entrySet();
        for (Map.Entry<Integer, String> s : entries) {
            System.out.println(s);
        }
    }
}
