package day02;

public class TestIAdd5 {
    public static void main(String[] args) {
        int a = 1;
        a = ++a;
        /*
        (1)先处理++a， a先自增1，a=2，然后取a的值2放一边
        (2)赋值 a=2
         */
        System.out.println("a = " + a);//a=2
        a = a++;
        /*
        (1)先处理a++， 先取a的值2，放一边，然后a要自增1，a=3
        (2)赋值 a=2
         */
        System.out.println("a = " + a);//a=2
    }
}
