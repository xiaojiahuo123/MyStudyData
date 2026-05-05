package day02;

public class TestFloatDouble {
    public static void main(String[] args) {
        double pi = 3.1415926355867245;
        System.out.println("double类型的pi = " + pi);
        //double类型的pi = 3.1415926355867243
        //大约是十进制科学计数法的小数点后15-16

        float pi2 = 3.1415926355867245F;
        System.out.println("float类型的pi2 = " + pi2);
        //float类型的pi2 = 3.1415927
        //大约是十进制科学计数法的小数点后7-8
    }
}
