package day_13;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class TestException {
    public static void main(String[] args) {
        try {
            //文件输入流，用于读取文件内容
            FileInputStream fis = new FileInputStream("d:\\1.txt");
        } catch (FileNotFoundException e) {
            System.out.println("执行失败");
        }

        //System.out.println(1/0);//编译器没有提示我们风险，运行时发生ArithmeticException算术异常
//        int[] arr = {1,2,3};
//        System.out.println(arr[5]);//编译器没有提示我们风险，运行时发生ArrayIndexOutOfBoundsException

        //  Object obj = "hello";//多态引用，父类Object的变量指向子类String的对象
        //  Integer num = (Integer) obj;//编译器没有提示我们风险，运行时发生ClassCastException
    }
}
