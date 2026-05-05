package day06_teacher_code.src;

import java.util.Scanner;

public class TestArrayInsert {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};

        //从键盘输入1个整数，插入到arr数组的[1]位置
        //（1）先扩容
        int[] newArr = new int[arr.length+1];//扩1个位置
        for(int i=0; i<arr.length; i++){//原样复制元素
            newArr[i] = arr[i];
        }
        arr = newArr;//抛弃旧数组，选用新数组

        //(2)把[1]位置及其后面的元素往右移动
        /*
        [4] -> [5]
        [3] -> [4]
        [2] -> [3]
        [1] -> [2]
         */
        for(int i=arr.length-1; i>1; i--){
            //arr[后面] = arr[前面];
            arr[i] = arr[i-1];
        }

        //（3）在[1]插入新元素
        Scanner input = new Scanner(System.in);
        System.out.print("请输入新元素：");
        int newNum = input.nextInt();

        arr[1] = newNum;

        input.close();

        //（4）遍历数组
        System.out.println("插入新元素之后：");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
    }
}
