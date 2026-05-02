package day06_teacher_code.src;

import java.util.Scanner;

public class MyLianxi_03 {
    public static void main(String[] args) {
//        在数组中查找目标值
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[100];
        String str =  "0";
        for (int i = 0; i < 100; i++) {
            arr[i] = (int)(Math.random() * 100);
            System.out.println(arr[i]);
        }
        System.out.println("请你输入需要查找的目标值（整数）：");
        int n = sc.nextInt();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == n) {
                str = ","+ i;
            }
        }
        if (str.equals("0")){
            str = "目标值不存在此数组中";
        }
        System.out.println("目标值"+n+","+"在数组中的"+str);
        sc.close();
    }

}
