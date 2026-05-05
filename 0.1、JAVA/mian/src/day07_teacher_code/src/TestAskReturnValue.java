package day07_teacher_code.src;

public class TestAskReturnValue {
    public static void main(String[] args) {
        int x = 1;
        int y = 2;
        sum1(x,y);
        int z = 3;

        //求x,y,z的和

        int result = sum2(sum2(x, y), z);
        System.out.println("result = " + result);
    }

    public static void sum1(int a, int b){
        System.out.println(a + " + " + b  + "= " + (a+b));
    }

    public static int sum2(int a, int b){
        return a + b;
    }
}
