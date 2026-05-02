package day02;

public class TestTypeChange5 {
    public static void main(String[] args) {
        int x = 1;
        int y = 2;
        System.out.println(x / y);//0 结果是int类型
        System.out.println((double)x/y);//0.5 把x的值1升级为double，double/int结果是double
        System.out.println((double)(x/y));//0.0
    }
}
