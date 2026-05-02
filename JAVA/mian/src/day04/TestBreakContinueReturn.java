package day04;

public class TestBreakContinueReturn {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            System.out.println("i=" + i + ",(1)");
            if (i == 3) {
                continue;//跳过i==3这次的(2)语句
            }
            System.out.println("i=" + i + ",(2)");
        }
        System.out.println("(3)");
    }
}
