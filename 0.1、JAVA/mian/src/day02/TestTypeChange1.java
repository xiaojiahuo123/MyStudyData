package day02;

public class TestTypeChange1 {
    public static void main(String[] args) {
        int num = 'a';
        /*
        'a'的字面量值是char类型
        num变量是int类型
        char占2个字节，int占4个字节
        char的范围小，int范围大
         */
        System.out.println("num = " + num);
        //num = 97

        double d = 1;
        /*
        1的字面量值是int类型
        d是double
        double > int
         */
        System.out.println("d = " + d);//d = 1.0


    }
}
