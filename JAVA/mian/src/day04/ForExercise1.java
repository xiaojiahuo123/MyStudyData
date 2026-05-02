package day04;

public class ForExercise1 {
    public static void main(String[] args) {
        //方式一：用if条件控制某些语句
        for(int i=1; i<=100; i++){//数字范围是[1,100]所有数
            if (i%2==0) {//满足偶数条件的情况
                System.out.println(i);
            }
        }

        //方式二：控制循环的次数是50次，以及参与循环的全部是偶数，非偶数不参与循环
        /*for(int i=2; i<=100; i+=2){
            System.out.println(i);
        }*/

        //写代码：先完成，再完美
    }
}
