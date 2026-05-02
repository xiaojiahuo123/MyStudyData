package day07_teacher_code.src;

public class TestParamDemo2 {
    public static void main(String[] args) {
        int x= 1;
        System.out.println("x = " + x);
        change(x);
        System.out.println("x = " + x);
    }

    public static void change(int a){
        ++a;
        a=100;
    }
}
