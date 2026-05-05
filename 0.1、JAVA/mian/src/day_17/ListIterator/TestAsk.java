package day_17.ListIterator;

import org.junit.Test;

import java.util.*;

public class TestAsk {
    @Test
    public void test1(){
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "a", "b", "c");
        ListIterator<String> iterator = list.listIterator();
        while(iterator.hasNext()){
//方法不调用不执行，调用一次执行一次
//下面调用了2次next()方法，每一次next都会取出当前迭代器位置的元素，然后迭代器往右移动一下
//迭代器移动异常 ：每次调用 next() 方法都会使迭代器前进一个位置
// - 元素访问错误 ：对于包含奇数个元素的集合，最后一次循环会尝试访问超出集合范围的元素，导致 NoSuchElementException
// - 逻辑错误 ：输出的结果不符合预期，会将第一个元素与第二个元素的长度组合
//简单的说，为了避免出现索引越界，在循环的条件做了设置，必须满足hasNext()方法返回true，但是循环体中的一次循环
//调用两次迭代器，导致了循环条件无法有效约束循环体了
        
           // System.out.println(iterator.next() +"的长度" + iterator.next().length());//错误
            System.out.println(iterator.next());
        }
    }

    @Test
    public void test2(){
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1,"hello");
        map.put(2,"world");
        map.put(3,"java");

        /*
        Map接口及其实现类，都没有实现Iterable接口，因此不能对Map及其实现类，直接使用foreach循环和Iterator迭代器进行遍历。
        只能将Map先转为Collection系列的集合。通过（1）keySet（2）values（3）entrySet方法转换
        Map与Collection类型无父子类关系，怎么能转换呢？
        因为这里的转换，不是强制类型转换。而是将元素重新组装到新的集合类型中。
         */
        Set<Map.Entry<Integer, String>> entries = map.entrySet();
        Iterator<Map.Entry<Integer, String>> iterator = entries.iterator();
        while(iterator.hasNext()){
            //现在Set中元素的类型是 Map.Entry类型，它有2个属性，属性的类型分别是Integer和String
            Map.Entry<Integer, String> s = iterator.next();
            System.out.println(s);
        }
    }
}
