package day03;

public class TestBitNegation {
    public static void main(String[] args) {
        System.out.println(~5);
        /*
        5的二进制补码：       00000000 00000000 00000000 00000101
        逐位取反（包括符号位）：11111111 11111111 11111111 11111010（十进制-6）
         */
    }
}
