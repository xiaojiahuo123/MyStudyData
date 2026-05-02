package day02;

public class TestCompare {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;

        System.out.println(a > b);//false
        System.out.println(a < b);//true
        System.out.println(a >= b);//false
        System.out.println(a <= b);//true
        System.out.println(a == b);//false
        System.out.println(a != b);//true

        System.out.println("==============================");
        System.out.println(a = b);//把b的值赋值给a
        System.out.println("a = " + a);//a=2
        System.out.println("b = " + b);//b=2
        //注意，= 和 == 的区别
    }
}
