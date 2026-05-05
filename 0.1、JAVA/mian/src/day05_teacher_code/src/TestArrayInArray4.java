package day05_teacher_code.src;

import java.util.Scanner;

public class TestArrayInArray4 {
    public static void main(String[] args) {
        /*
        第1个小组有5个人
        第2个小组有3个人
        第3个小组有4个人
         */
        int[][] arr = new int[3][];
        //这里只确定了一共有3行/组，但是没有确定每一组有几个人
        arr[0] = new int[5];
        //这句代码的作用是确定第1组有5个人
        //如果是数组名后面[]中有数字，代表下标，例如：arr[0]，这个[0]是下标
        //如果是数据类型后面[]中有数字，代表长度，例如：int[3]，这个[3]是长度
        arr[1] = new int[3];
        arr[2] = new int[4];
        //以上3句代码不能少，少了就会发生NullPointerException空指针异常

        Scanner input = new Scanner(System.in);

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print("请输入第" + (i+1)+ "组第" + (j+1) +"个同学的成绩：");
                arr[i][j] = input.nextInt();
            }
        }

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }


        input.close();
    }
}
