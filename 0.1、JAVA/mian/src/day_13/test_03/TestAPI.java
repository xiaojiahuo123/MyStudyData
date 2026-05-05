package day_13.test_03;

import org.junit.Test;

import java.util.Arrays;
import java.util.Comparator;

public class TestAPI {
    
    @Test
    public void test1(){
        System.out.println("int整数的最大值：" + Integer.MAX_VALUE);
        System.out.println("int整数的最小值：" + Integer.MIN_VALUE);
        /*
        int整数的最大值：2147483647
        int整数的最小值：-2147483648
         */
    }

    @Test
    public void test2(){
        Employee[] arr = new Employee[4];
        arr[0] = new Employee(2,"张三",15000,23);
        arr[1] = new Employee(1,"李四",16000,26);
        arr[2] = new Employee(3,"王五",12000,27);
        arr[3] = new Employee(4,"赵六",19000,21);

        System.out.println("按照id升序排序：");
        //直接使用java.util.Arrays工具类
        Arrays.sort(arr);//会按照元素的compareTo方法来比较两个对象的大小

        //增强for
        for (Employee e : arr) {
            System.out.println(e);
        }

        System.out.println("按照年龄升序排序：");
        //按照年龄排序，从小到大
        Comparator c = new Comparator(){
            @Override
            public int compare(Object o1, Object o2) {
                Employee e1 = (Employee) o1;
                Employee e2 = (Employee) o2;
//                return e1.getAge() - e2.getAge();
                return Integer.compare(e1.getAge(),e2.getAge());//作用与上面相减的相同
            }
        };
        Arrays.sort(arr, c);//让它用c对象的compare方法来比较两个员工对象的大小
        //再次遍历
        for (Employee e : arr) {
            System.out.println(e);
        }

        System.out.println("按照薪资升序排序：");
        Comparator c2 = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Employee e1 = (Employee) o1;
                Employee e2 = (Employee) o2;
                /*if(e1.getSalary() > e2.getSalary()){
                    return 1;
                }else if(e1.getSalary() < e2.getSalary()){
                    return -1;
                }
                return 0;*/
                return Double.compare(e1.getSalary(),e2.getSalary());
            }
        };
        Arrays.sort(arr, c2);//让它用c2对象的compare方法来比较两个员工对象的大小
        //再次遍历
        for (Employee e : arr) {
            System.out.println(e);
        }
    }

    @Test
    public void test4(){
        //整数 -> String
        int num = 1;
        String str = num + "";
        String str2 = String.valueOf(num);

        //String -> int
        String str3 = "123";
        String str4 = "456";
        System.out.println(str3 + str4);//拼接 123456
        int a = Integer.parseInt(str3);
        int b = Integer.parseInt(str4);
        System.out.println(a + b);//求和
    }

    @Test
    public void test5(){
        String s1 = "3.14";
        String s2 = "6.36";
        double d1 = Double.parseDouble(s1);
        double d2 = Double.parseDouble(s2);
        System.out.println(d1 + d2);
    }
}
