package day04;

public class ForExercise2 {
    public static void main(String[] args) {
        //2、所谓水仙花数是指一个3位数，其各个位上数字立方和等于其本身。
        // 例如： 153 = 1*1*1 + 5*5*5 + 3*3*3，
        // 找出所有的水仙花数，并统计他们有几个。
/*
这道题需要注意的：
（1）百位、十位、个位的求法，运算符的应用
（2）变量和语句是不是应该在循环中，
放到循环for的{}一定是需要重复，反复执行的语句
 */

        //水仙花数是指一个3位数 => 循环的范围 [100, 999]
        int count = 0;
        for(int i=100; i<=999; i++){
            //求各个位上数字，百位、十位、个位
            int bai = i / 100;
//            int shi = i / 10 % 10;
            int shi = i % 100 / 10;
            int ge = i % 10;


    /*        System.out.println("bai = " + bai);
            System.out.println("shi = " + shi);
            System.out.println("ge = " + ge);*/

            if(bai * bai * bai + shi * shi *shi + ge * ge * ge == i){
                System.out.println(i);
                count++;

            }

        }

        System.out.println("一共有：" + count);
    }
}
/*
学习基础有两个目标：
1、基本语法（死的规定）
2、编程思维的锻炼
 */