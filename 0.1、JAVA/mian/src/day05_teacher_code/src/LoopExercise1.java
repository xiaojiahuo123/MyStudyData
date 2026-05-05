package day05_teacher_code.src;

public class LoopExercise1 {
    public static void main(String[] args) {
        for(int i = 1; i<=9; i++){
            /*
            当i=1，打印1个式子
            当i=2，打印2个式子
            ...
            当i=9，打印9个式子
             */
            for(int j=1; j<=i; j++){
//                System.out.print("式子\t");
                System.out.print(j +"*" + i + "=" + j*i + "\t");
            }
            System.out.println();
        }
        /*
        i=1; i<=9;成立
            j=1; j<=1; 成立  输出 1*1=1
            j++,j=2; j<=1不成立 结束内循环
            换行
        i++;i=2; i<=9;成立
            j=1; j<=2;成立  输出 1*2=2;
            j++; j<=2;成立  输出 2*2=2;
            j++;j=3;j<=2不成立
            换行
        i++; i=3; i<=9成立
            ....
         */
    }
}
