package day04;

public class TestFor2 {
    public static void main(String[] args) {
        //使用for循环，实现求1-100的整数和
        int sum = 0;
        for(int i=1; i<=100; i++){
            sum += i;
        }
        System.out.println("sum = " + sum);
    }
}
