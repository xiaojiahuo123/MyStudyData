package day07_teacher_code.src;

public class TestRecursion {
    public static void main(String[] args) {
        //求n!
        /*
        假设：f(n)代表n!
            f(n) = n * f(n-1)
         */
        System.out.println(f(5));
        System.out.println(loop(5));

    }

    public static int f(int n){
        if(n>1) {
            return n * f(n - 1);//自己调用自己就叫递归
        }
        return 1;
    }

    public static int loop(int n){
        int result = 1;
        for(int i=n; i>=1; i--){
            result *= i;
        }
        return result;
    }
}
