package day02;

public class TestIAdd3 {
    public static void main(String[] args) {
        int a = 1;
        int b = a++;//自增不是独立的运算，与赋值在一起
        /*
        (1)处理a++， 先取a的值1放一边（用专业的话说，放操作数栈），然后a自增1，a=2，  总结：先取值后自增
        (2)把刚才取出来的值，赋值给b
         */
        System.out.println("a = " + a);//a=2
        System.out.println("b = " + b);//b=1

        int c = ++a;
        /*
        (1)处理++a， 先对a自增1，a=3，然后取a的值3放一边（用专业的话说，放操作数栈）  总结：先自增再取值
        (2)把刚才取出来的值，赋值给c
         */
        System.out.println("a = " + a);//a=3
        System.out.println("c = " + c);//c=3
    }
}
