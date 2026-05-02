package day02;

public class TestCompare2 {
    public static void main(String[] args) {
        String s1 = "hello";
        String s2 = "hello";
        System.out.println(s1 == s2);//true  比较地址值

        String s3 = "hellohello";
        String s4 = s1 + s2;
        System.out.println(s3 == s4);//false   比较地址值
        System.out.println("s3 = " +s3);
        System.out.println("s4 = " +s4);

//        System.out.println(s1 > s2);//报错
    }
}
