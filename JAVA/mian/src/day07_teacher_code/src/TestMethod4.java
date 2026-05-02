package day07_teacher_code.src;

public class TestMethod4 {

    //功能：求两个整数a,b的和
    public static int add(int a, int b){//有参
        return a + b;
    }

    //功能：打印"hello"到控制台
    public static void sayHello(){//无参
        System.out.println("hello");
    }

    public static void main(String[] args) {
        //(5,3)是实际参数，简称实参，它们的作用是给形参(a,b)赋值/传值/传参
        int result = add(5, 3);//用result变量接收add方法的结果，返回值
        System.out.println("result = " + result);

        sayHello();
    }
}
