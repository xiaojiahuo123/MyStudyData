package day04;

public class TestBreakContinueReturn3 {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            System.out.println("i=" + i + ",(1)");
            if (i == 3) {
               return;
            }
            System.out.println("i=" + i + ",(2)");
        }
        System.out.println("(3)");
    }
}
