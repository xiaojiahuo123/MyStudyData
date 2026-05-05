package day_16.Map的增删改查;

import org.junit.Test;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class TestMap5 {
    @Test
    public void test1(){
        HashMap<String,String> map = new HashMap<>();
        map.put("小孙", "10086");//添加一对键值对
        map.put("老王", "10010");

//        Set集合的元素不可以重复，因为key不能重复
        Set<String> Keys = map.keySet();//通过keySet()方法，获取map中所有的key
//        public Set<K> keySet() {
//            Set<K> ks = keySet;
//            if (ks == null) {
//                ks = new HashMap.KeySet();
//                keySet = ks;
//            }
//            return ks;
//        }
        for (String key : Keys) {
            System.out.println(key + "对应的Value值为 ："+map.get(key));
        }
    }

    @Test
    public void test2(){
        HashMap<String, String> map = new HashMap<>();

        map.put("小孙", "10086");//添加一对键值对
        map.put("老王", "10086");
        System.out.println(map);


        //方式二：遍历所有的value
        Collection<String> values = map.values();
        for (String value : values) {
            System.out.println(value);
        }
/*        public Collection<V> values() {
            Collection<V> vs = values;
            if (vs == null) {
                vs = new HashMap.Values();
                values = vs;
            }
            return vs;
        }*/
    }

    @Test
    public void test3(){
        //HashMap<String, String> map = new HashMap<>();
        Map<String, String> map = new HashMap<>();
        
        map.put("小孙", "10086");//添加一对键值对
        map.put("老王", "10086");
        System.out.println(map);

        //方式三：遍历所有的键值对
        Set<Map.Entry<String, String>> entries = map.entrySet();
        //最外层是Set表示，所有的(key,value)的映射关系不会重复
        //Entry是Map中的接口，HashMap由于是Map的子类，因为多态的原因会先找
        //内层是 Map.Entry，它是所有(key,value)键值对的公共父接口类型
        //因为Entry接口是Map接口的内部接口，所以名字上写的是Map.Entry
        for (Map.Entry<String, String> entry : entries) {//一个entry代表一个键值对
//            System.out.println(entry);
            System.out.println("key:" + entry.getKey() +"\tvalue = " +entry.getValue());
        }
    }
}
