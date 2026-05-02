package day07_teacher_code.src;

public class TestMethod8 {
    //功能：求任意两个整数的最大值
    public static int max(int a, int b){//有参有返回值
        return a > b ? a : b;
    }

    public static void main(String[] args) {
        int x = 4;
        int y = 5;
        int z = 12;

        int bigger = max(x, y);
        System.out.println("bigger = " + bigger);
        int biggest = max(bigger, z);
        System.out.println("biggest = " + biggest);
    }
}
