package day04;

public class TestFor1 {
    public static void main(String[] args) {
/*        for(;;) {//是循环，但是它是死循环，无限循环，通常是需要我们避免的
            System.out.println("我爱尚硅谷");
        }*/

        /*for(int i=1; i<=5; i++){
            System.out.println("我爱尚硅谷" + i);
        }*/
        /*
        int i=1; i<=5; 成立 System.out.println("我爱尚硅谷");
        i++; i=2; i<=5; 成立 System.out.println("我爱尚硅谷");
        i++; i=3; i<=5; 成立 System.out.println("我爱尚硅谷");
        i++; i=4; i<=5; 成立 System.out.println("我爱尚硅谷");
        i++; i=5; i<=5; 成立 System.out.println("我爱尚硅谷");
        i++; i=6; i<=5; 不成立，结束for
         */
        /*int i;
        for(i=1; i<=5; i++){
            System.out.println("我爱尚硅谷" + i);
        }
        System.out.println("i = " + i);*/


        for(int i=1; i>=5; i++){
            System.out.println("我爱尚硅谷" + i);
        }
        //int i=1; i>=5; 不成立
    }
}
