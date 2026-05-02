package day05_teacher_code.src;

public class LoopExercise3 {
    public static void main(String[] args) {
        //把菱形分为2半，上半部分和下半部分
        /*
        上半部分：5行
        i=1，打印4个空格，1个*，换行
        i=2，打印3个空格，3个*，换行
        i=3，打印2个空格，5个*，换行
        i=4，打印1个空格，7个*，换行
        i=5，打印0个空格，9个*，换行
         */
        for(int i=1; i<=5; i++){
            //打印n个空格
            for(int j=1; j<=5-i; j++){
                System.out.print("  ");
            }
            //打印m个*
            for(int j=1; j<=2*i-1; j++){
                System.out.print("* ");
            }
            //换行
            System.out.println();
        }

        /*
        下半部分：4行
        i=1，打印1个空格，7个*，换行
        i=2，打印2个空格，5个*，换行
        i=3，打印3个空格，3个*，换行
        i=4，打印4个空格，1个*，换行
         */
        for(int i=1; i<=4; i++){
            //打印n个空格
            for(int j=1; j<=i; j++){
                System.out.print("  ");
            }
            //打印m个*
            for(int j=1; j<=9-2*i; j++){
                System.out.print("* ");
            }
            //换行
            System.out.println();
        }
    }
}
