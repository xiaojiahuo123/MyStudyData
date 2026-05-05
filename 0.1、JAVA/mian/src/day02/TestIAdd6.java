package day02;

public class TestIAdd6 {
    public static void main(String[] args) {
        int a = 1;
        int b = a++ + ++a * a++;
        /*
        (1)先处理 a++   先取a的值1放一边， 紧接着a自增为2
        (2)处理 ++a     先对a自增1，a=3，然后取a的值3放一边
        (3)因为要先算乘法，乘法需要两个操作数，处理a++    先取a的值3放一边， 紧接着a自增为4
        (4)算乘法  3 * 3 = 9
        (5)算加法 1+9=10
        (6)赋值 b = 10
         */
        System.out.println("a = " + a);//a=4
        System.out.println("b = " + b);//b=10
    }
}
