package day03;

import java.util.Scanner;

public class TestIfElseIf2 {
    public static void main(String[] args) {
        /*
        从控制台输入1个成绩，成绩应该在[0,100]之间
        当成绩为100分时，输出满分
        当成绩为80-99时，输出优秀
        当成绩为70-79时，输出良好
        当成绩为60-69时，输出及格
        60分以下，输出不及格
         */
        Scanner input = new Scanner(System.in);

        System.out.print("请输入成绩：");
        int score = input.nextInt();

        //当多个分支只会执行其中1个分支时，我们需要采用多分支结构
        if(score < 0 || score > 100){
            System.out.println("成绩输入有误，成绩应该在[0,100]之间！");
        }else if(score == 100){
            System.out.println("满分");
        }else if(score>=70){
            System.out.println("良好");
        }else if(score>=80){
            System.out.println("优秀");
        }else if(score>=60){
            System.out.println("及格");
        }else{
            System.out.println("不及格");
        }

        input.close();

    }
}
