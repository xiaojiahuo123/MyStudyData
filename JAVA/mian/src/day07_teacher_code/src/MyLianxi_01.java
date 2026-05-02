package day07_teacher_code.src;

public class MyLianxi_01 {
    public static void main(String[] args) {
        //把光标放到调用方法的()里面，按快捷键Ctrl + p
        System.out.println(max(4,6));
        System.out.println(max(4.0,6.0));
        System.out.println(max(4,5,2));

        System.out.println(max(4,6.0));
//        System.out.println(max(4.0,6.0,7.0));//找不到最匹配的，也找不到可以兼容的，就报错了
    }

    //求两个整数的最大值
    public static int max(int a, int b) {
        return Math.max(a, b);
    }

    //求3个整数的最大值
    public static int max(int a, int b, int c) {
        int max = Math.max(a, b);
        return Math.max(max, c);
    }

    //求两个小数的最大值
    public static double max(double a, double b) {
        return Math.max(a, b);
    }
}
