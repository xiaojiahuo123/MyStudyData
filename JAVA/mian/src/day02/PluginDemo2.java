package day02;

public class PluginDemo2 {
    public static void main(String[] args) {
        //有3个int类型的变量，求它们的最大值
        int a = 10;
        int b = 20;
        int c = 30;
        //int max = a;
//        if (b > max) {
//            max = b;
//        }
//        if (c > max) {
//            max = c;
//        }
//
       int max = a > b? a : b;
       max = max > c? max : c;
        System.out.println("max = " + max);
    }
}
