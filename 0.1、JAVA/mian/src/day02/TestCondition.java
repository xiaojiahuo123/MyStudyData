package day02;

public class TestCondition {
    public static void main(String[] args) {
        int x = 4;
        int y = 3;

//        x > y ? x : y;//错误，条件运算符计算完的结果没有用起来
      //  int max;
       // x > y ? max = x : max = y;//错误

        int max = x > y ? x : y;
        System.out.println("max = " + max);

        System.out.println("最大值是" + (x > y ? x : y));
        System.out.println(x > y ? x : y);

        System.out.println("===================");

        int m = 5;
        int n = 4;
        int p = 6;

        int biggest = m>n?m:n;//biggest是m,n中的最大值
        biggest = biggest > p ? biggest : p;//3个数中的最大值
        System.out.println("biggest = " + biggest);
        /*
        对于程序员的要求：
        （1）完成功能
        （2）考虑可读性
        （3）考虑效率，性能（内存和时间）

        先保证（1）能实现，在（1）已经比较轻松的情况下，想想（2）
        （1）（2）都没问题，再想（3）
         */

    }
}
