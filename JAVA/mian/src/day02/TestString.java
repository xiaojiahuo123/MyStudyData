package day02;

public class TestString {
    public static void main(String[] args) {
        System.out.println("a" + 'b' + 'c');//abc
        /*
        "a" + 'b' 是拼接 得到 "ab"
        "ab" + 'c' 还是拼接，得到"abc"
         */

        System.out.println('a' + 'b' + 'c');
        //294 = 97 + 98 +99
        System.out.println('a' + 'b' + "c");
        //97 + 98 = 195
        //195 +"c" 拼接
        /*
        凡是+的左右出现字符串，+就是拼接，结果还是字符串
        凡是+的左右都不是字符串，+就是求和，用数字来算
         */
    }
}
