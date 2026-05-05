package day_18.StreamAPI;

import org.junit.Test;

import java.util.ArrayList;
import java.util.function.Consumer;
import java.util.function.Predicate;
import java.util.stream.Stream;

public class TestStudent {
    @Test
    public void test1(){
        ArrayList<Student> list = new ArrayList<>();
        list.add(new Student(1,"Lucy"));
        list.add(new Student(2,"Lily"));
        list.add(new Student(3,"Alice"));
        list.add(new Student(4,"Tom"));

        System.out.println("流处理过程和结果：");
        Stream<Student> stream = list.stream();//创建了一个Stream
        //中间处理：筛选出名字中包含i字母的学生对象
        Predicate<Student> p = new Predicate<>() {
            @Override
            public boolean test(Student s) {
                return s.getName().contains("i");
            }
        };//匿名内部类写法
        stream.filter(p).forEach(System.out::println);

        // Consumer<Student> c = new Consumer<Student>() {
        //     @Override
        //     public void accept(Student student) {
        //         System.out.println(student);
        //     }
        // };//匿名内部类写法
        // stream.forEach(c);

        //stream.forEach(System.out::println);//方法引用

        System.out.println("处理之后：" +  list);
    }
}
