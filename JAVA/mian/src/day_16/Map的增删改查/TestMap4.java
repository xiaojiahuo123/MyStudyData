package day_16.Map的增删改查;

import org.junit.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TestMap4 {

    @Test
    public  void test1(){
        Map<String,String> map = new HashMap<>();
        map.put("小孙", "10086");//添加一对键值对
        map.put("老王", "10010");
        System.out.println("使用查询K值获取Value"+map.get("小孙"));
    }

    @Test
    public  void test2(){
        Map<Student,String> map = new HashMap<>();
        
        // 高级方式1：使用Stream API创建并添加Student对象
//        ArrayList<Student> arrayList = Stream.of(
//                new Student("小孙", 20, 90, "北京"),
//                new Student("老王", 25, 85, "上海"),
//                new Student("小李", 22, 95, "广州")
//        ).collect(Collectors.toCollection(ArrayList::new));
        
         //高级方式2：使用Java 9+ List.of()配合ArrayList构造器
         ArrayList<Student> arrayList = new ArrayList<>(List.of(
                 new Student("小孙", 20, 90, "北京"),
                 new Student("老王", 25, 85, "上海"),
                 new Student("小李", 22, 95, "广州")
         ));
        
        // 高级方式3：使用Stream API遍历并添加到map
        arrayList.forEach(student -> {
            map.put(student, student.getName().equals("小孙") ? "10086" : 
                               student.getName().equals("老王") ? "10010" : "10000");
        });

        //System.out.println(, map.get());
        // 高级方式：使用Stream API遍历输出
        System.out.println("ArrayList中的学生信息：");
        arrayList.forEach(student -> 
            System.out.printf("姓名：%s, 年龄：%d, 分数：%d, 地址：%s%n", 
                    student.getName(), student.getAge(), student.getScore(), student.getAddress())
        );
        
        // 高级方式：使用Stream API查询并输出
        System.out.println("\n通过Student对象查询map中的值：");
        arrayList.stream()
                .filter(student -> student.getName().equals("小孙"))
                .findFirst()
                .ifPresent(student -> 
                    System.out.println(student.getName() + "的联系电话：" + map.get(student))
                );
    }
}
