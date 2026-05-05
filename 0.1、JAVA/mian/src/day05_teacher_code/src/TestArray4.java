package day05_teacher_code.src;

import java.util.Scanner;

public class TestArray4 {
    public static void main(String[] args) {
        //从控制台接收用户输入的小组人数，以及每一个小组成员的成绩
        Scanner input = new Scanner(System.in);

        System.out.print("请输入本组学员的人数：");
        int count = input.nextInt();

        //定义（定义和声明是相同的概念）数组，长度为count，元素类型是int 或 double，这里用int演示
        int[] scores = new int[count];
        for (int i = 0; i < scores.length; i++) {
            System.out.print("请输入第" + (i+1) +"个同学的成绩：");
            scores[i] = input.nextInt();//从控制台接收的成绩放到元素中
        }

        System.out.println("所有同学的成绩如下：");
        for (int i = 0; i < scores.length; i++) {
            System.out.print(scores[i]+" ");
        }
        System.out.println();


        input.close();
    }
}
