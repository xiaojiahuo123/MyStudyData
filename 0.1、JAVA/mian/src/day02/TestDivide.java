package day02;

public class TestDivide {
    public static void main(String[] args) {
        //System.out.println(1/0);//编译通过，运行会发生ArithmeticException算术异常
        System.out.println(8.0 /2.4);
        System.out.println(8.0 / 0.0);//Infinity 无穷
    }
}
