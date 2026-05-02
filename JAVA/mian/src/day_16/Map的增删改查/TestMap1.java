package day_16.Map的增删改查;

import org.junit.Test;

import java.util.*;

public class TestMap1 {
    @Test
    public void test1() {
        HashMap<String, Integer> map1 = new HashMap<>();
        map1.put("张三", Integer.valueOf(89));  // 显式转换为 Integer
        map1.put("张三", Integer.valueOf(89));
        //HashMap是不允许重复的键值对的，
/*        当执行map1.put("张三", ...)时，HashMap 会先计算 “张三” 的 hashCode，找到对应的存储桶；
        再通过equals()方法，判断桶中已有的键是否与 “张三” 相等；
        若相等（即键重复），则直接用新的 Value 替换该键对应的旧 Value，不会新增键值对；
        只有当键的hashCode和equals都不匹配时，才会新增元素。*/
        System.out.println(map1);
        Vector v1 = new Vector();
        v1.add("asdadad");
        System.out.println(v1);
    }
}
