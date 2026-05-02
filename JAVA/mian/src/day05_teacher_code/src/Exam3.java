package day05_teacher_code.src;

public class Exam3 {
    public static void main(String[] args) {
        //题3：使用循环实现累加1-100之间3的倍数的和
        int sum = 0;
        for(int i=1; i<=100; i++){
            if(i%3==0){
                sum += i;
            }
        }
        System.out.println("sum = " + sum);

        System.out.println("====================");
        int he = 0;
        for(int i=3; i<=100; i+=3){
            he += i;
        }
        System.out.println("he = " + he);
    }
}
