package day04;

public class TestLoopInLoop3 {
    public static void main(String[] args) {
        /*

        *
        * *
        * * *
        * * * *
        * * * * *

         */
        for(int i=1; i<=5; i++){
            /*
            i=1，需要打印1个*
            i=2，需要打印2个*
            ...
            i=5，需要打印5个*
             */
            for(int j=1; j<=i; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
