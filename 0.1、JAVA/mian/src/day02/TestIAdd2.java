package day02;

public class TestIAdd2 {
    public static void main(String[] args) {
        int a = 1;
        //以下写法++。--在前在后没区别
        a++;
        System.out.println("a = " + a);//a=2
        ++a;
        System.out.println("a = " + a);//a=3

        a--;
        System.out.println("a = " + a);//a=2
        --a;
        System.out.println("a = " + a);//a=1
    }
}
