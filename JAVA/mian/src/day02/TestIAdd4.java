package day02;

public class TestIAdd4 {
    public static void main(String[] args) {
        int a = 1;
        System.out.println(a++);//1   先取值1放一边，然后自增a=2
        System.out.println(a);//2
        System.out.println(++a);//3  先自增1,a=3，再取值输出
        System.out.println(a);//3
    }
}
