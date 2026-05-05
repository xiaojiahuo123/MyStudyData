package day02;

public class TestTypeChange4 {
    public static void main(String[] args) {
        int num = (int) 5.8;//代表报错的时候，光标移动到错误处，按快捷键Alt + Enter，会给你一些建议
        System.out.println("num = " + num);//num = 5

        byte b = (byte) 200;
        System.out.println(b);//-56
        /*
        200是int类型，二进制 00000000  00000000 00000000 11001000
        转为byte，只有1个字节，截取最后一个字节：  11001000（最高位是1，是负数）
                            补码：11001000
                            反码：11000111
                            原码：10111000
                            8 + 16 + 32 = 56
                            最高位1代表负数，-56
                            人工用权值相加法时，需要用原码算。
                            计算器不用这么麻烦，直接根据补码就可以得到结果
         */

        byte b2 = (byte) 128;
        /*
        128是int类型，二进制 00000000  00000000 00000000 10000000
        转为byte，只有1个字节，截取最后一个字节： 10000000
                    它需要单独记  -128
         */
    }
}
