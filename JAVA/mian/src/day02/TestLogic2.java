package day02;

public class TestLogic2 {
    public static void main(String[] args) {
        boolean flag = true;
        System.out.println(!flag);//false

        //判断a变量是不是偶数
        int a = 8;
        System.out.println("a是不是偶数？" + (a%2==0)); //能被2整除吗
        System.out.println("a是不是偶数？" + !(a%2!=0));//不是奇数吗
    }
}
