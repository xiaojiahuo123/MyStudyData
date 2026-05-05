package day07_teacher_code.src;

public class TestMethodMemory {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;
        add(a,b);
        int result = add(a, b);
        System.out.println("result = " + result);
    }

    public static int add(int a, int b){
        int sum = a + b;
        return sum;
    }
}
