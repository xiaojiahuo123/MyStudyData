package day06_teacher_code.src;

import java.util.Scanner;

public class TestArrayOrderFind {
    public static void main(String[] args) {
        int[] arr = {5, 6, 2, 7, 8, 1, 3};

        //从键盘输入一个整数，看它在不在数组中
        Scanner input = new Scanner(System.in);

        System.out.print("请输入一个整数：");
        int target = input.nextInt();//7  or  9

        //用target与数组的元素“一一比较”，确定是否存在
        boolean flag = false;//假设它不存在，flag是一个标记值，false代表不存在，true代表存在
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == target){
                flag = true;
                break;
            }
        }

       if(flag){// if(flag==true){
            System.out.println("找到了");
        }else{
            System.out.println("没找到");
        }

        input.close();
    }
}
