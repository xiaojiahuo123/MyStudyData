package day04;

public class TestBreakContinueReturn2 {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            System.out.println("i=" + i + ",(1)");
            if (i == 3) {
                break;//当i==3时直接结束for循环
            }
            System.out.println("i=" + i + ",(2)");
        }
        System.out.println("(3)");
    }
}
