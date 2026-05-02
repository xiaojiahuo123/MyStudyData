package day04;

public class TestLoop {
    public static void main(String[] args) {
        //从1开始累加整数，1+2+3....，求使得累加和到达或超过100的最小n值
/*        int n = 1;
        int sum = 0;
        while(sum < 100){
            sum += n;
            n++;
        }
        System.out.println("sum = " + sum);
        System.out.println("最小n值：" + (n-1));*/

        System.out.println("=================");

        /*int sum = 0;
        int n;
        for(n = 1; sum < 100; n++){
            sum += n;
        }
        System.out.println("sum = " + sum);
        System.out.println("最小n值：" + (n-1));*/

        System.out.println("===============");
        int n = 1;
        int sum = 0;
        do{
            sum += n;
            n++;
        }while(sum < 100);
        System.out.println("sum = " + sum);
        System.out.println("最小n值：" + (n-1));
    }
}
