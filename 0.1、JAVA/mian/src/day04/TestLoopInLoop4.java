package day04;

public class TestLoopInLoop4 {
    public static void main(String[] args) {
        /*
            *
           ***
          *****
         *******
        *********
         */
        for(int i=1; i<=5; i++){
            //打印空格
            /*
            当i=1，打印4个空格
            当i=2，打印3个空格
            当i=3，打印2个空格
            当i=4，打印1个空格
            当i=5，打印0个空格
             */
            for(int j=1; j<=5-i; j++){
                System.out.print("  ");
            }
            /*
            //打印*
            i=1，需要打印1个*
            i=2，需要打印3个*
            i=3，需要打印5个*
            i=4，需要打印7个*
            i=5，需要打印9个*
             */
            for(int j=1; j<=2*i - 1; j++){
                System.out.print("* ");
            }
            //换行
            System.out.println();
        }
    }
}
