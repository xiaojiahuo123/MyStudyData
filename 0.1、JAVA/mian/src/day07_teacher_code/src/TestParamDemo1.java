package day07_teacher_code.src;

public class TestParamDemo1 {
    public static void main(String[] args) {
        int x = 1;
        int y = 2;
        System.out.println("x = " + x +"，y = " + y );
        swap(x,y);
        System.out.println("x = " + x +"，y = " + y );
    }

    public static void swap(int a, int b){
        int temp = a;
        a = b;
        b = temp;
    }
}
