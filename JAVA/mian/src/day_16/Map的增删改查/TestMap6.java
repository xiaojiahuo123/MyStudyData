package day_16.Map的增删改查;

import org.junit.Test;

import java.util.ArrayList;
import java.util.HashMap;

public class TestMap6 {
    @Test
    public void test1(){
        //存储咱们班的男同学及其女朋友
        HashMap<String, String> map = new HashMap<>();
        map.put("小孙", "翠花");
        map.put("小孙", "如花");
        map.put("小孙", "花花");
        System.out.println(map);
    }

    @Test
    public void test2(){
        //存储咱们班的男同学及其女朋友
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        ArrayList<String> girls = new ArrayList<>();
        girls.add("翠花");
        girls.add("如花");
        girls.add("花花");
        map.put("小孙", girls);
        map.put("小司",null);

        System.out.println(map);
    }
}
