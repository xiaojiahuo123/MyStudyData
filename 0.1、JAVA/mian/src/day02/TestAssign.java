package day02;

public class TestAssign {
    public static void main(String[] args) {
        int a = 1;
        a += 1;// a = a + 1;
        System.out.println(a);//a=2

        int b = 1;
        a *= a + b;//a = a * (a+b) = 2 * (2+1) = 6
        System.out.println("b = " + b);//b=1
        System.out.println("a = " + a);//a=6

        byte b1 = 127;
        byte b2 = 2;
//        b1 = b1 + b2;//错误，b1+b2会升级为int
        b1 += b2;// b1 = (byte)(b1 + b2);
        System.out.println("b1 = " +b1);//b1 = -127
        /*
        b1+b2=129 的二进制 00000000 00000000 00000000 10000001
        截断              10000001  符号位是1，是负数
        如果是计算器看结果，10000001（补码）直接放到二进制的位置即可
        如果是人工计算，用权值相加法，需要换算原码
                    10000001（补码）
                    10000000（反码）
                    11111111（原码）
                    最左边的1，表示负数
                    剩下的1，权值相加法 1111111
                          1+2+4+8+16+32+64=127
         */
    }
}
