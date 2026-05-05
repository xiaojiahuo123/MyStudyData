package day02;

public class TestChar {
    public static void main(String[] args) {
        System.out.println(1);//int类型的1
        System.out.println('1');//char类型的'1'
/*
        1    00000000 00000000 00000000 00000001 （int占4个字节）
底层：以2个字节为例
        1    00000000 00000001（以2个字节为例）
        '1'  00000000 00110001
 */
        System.out.println(1 + 0); //1
        System.out.println('1' + 0 );//49
    }
}
