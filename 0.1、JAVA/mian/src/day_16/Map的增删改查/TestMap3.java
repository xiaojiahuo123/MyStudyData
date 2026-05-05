package day_16.Map的增删改查;

import org.junit.Test;

import java.util.HashMap;
import java.util.function.BiFunction;

public class TestMap3 {
    @Test
    public void test1(){
        HashMap<String, String> map = new HashMap<>();

        map.put("小孙", "10086");//添加一对键值对
        map.put("老王", "10010");

        map.replace("小孙","110"); //等价于 map.put("小孙" ,"110");  根据key覆盖原来的value
        System.out.println(map);//{小孙=110, 老王=10010}
    }

    @Test
    public void test2(){
        HashMap<String, String> map = new HashMap<>();

        map.put("小孙", "10086");//添加一对键值对
        map.put("老王", "10010");

        map.replace("小孙","10086","110");
        map.replace("老王","10086","120");
        //要求key和旧value都对应，才会用新的value覆盖原来的value
        System.out.println(map);
    }

    @Test
    public void test3(){
        HashMap<String, String> map = new HashMap<>();

        map.put("小孙", "10086");//添加一对键值对
        map.put("老王", "10010");

        /*
        replaceAll方法的形参：BiFunction<? super K, ? super V, ? extends V> （使用）
        BiFunction接口的原型 BiFunction<T, U, R> 抽象方法  R apply(T t, U u); （声明）
        现在结合它俩：
                现在的抽象方法  新Value的类型 apply(Key的类型， 旧Value的类型)

            //假设我这里想要在所有value值前面拼接上 "010-"
         */
        BiFunction<String,String,String> bi = new BiFunction<String, String, String>() {
            @Override
            public String apply(String key, String oldValue) {
                return "010-" + oldValue;
            }
        };

        map.replaceAll(bi);
        System.out.println(map);
    }

    @Test
    public void test4(){
        //存储学号 对应 英文名
        HashMap<Integer, String> map = new HashMap<>();

        map.put(Integer.valueOf(1), "irene");//添加一对键值对
        map.put(Integer.valueOf(2), "lucy");
        map.put(Integer.valueOf(3), "lily");
        map.put(Integer.valueOf(4), "alice");

        /*
        replaceAll方法的形参：BiFunction<? super K, ? super V, ? extends V> （使用）
        BiFunction接口的原型 BiFunction<T, U, R> 抽象方法  R apply(T t, U u); （声明）
        现在结合它俩：
                现在的抽象方法  新Value的类型 apply(Key的类型， 旧Value的类型)

            假设我这里想要把 key为偶数的键值对的 value的值改为大写
         */
        BiFunction<Integer,String,String> bi = new BiFunction<>() {
            @Override
            public String apply(Integer key, String oldValue) {
                return key%2==0 ? oldValue.toUpperCase() : oldValue;
            }
        };

        map.replaceAll(bi);
        System.out.println(map);
    }
}
