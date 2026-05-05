package day04;

public class TestLoopInLoop1 {
    public static void main(String[] args) {
        /*
        1 1 1 1 1
        2 2 2 2 2
        3 3 3 3 3
        4 4 4 4 4
         */
        for(int i=1; i<=4; i++){//控制行数
//            5次的i值的打印
            for(int j=1; j<=5; j++){//控制5次的i值的打印
                System.out.print(i+" ");
            }
            System.out.println();//换行
        }
    }
}
