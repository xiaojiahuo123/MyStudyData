package day06_teacher_code.src;

import java.util.Scanner;

public class TestArrayGrow {
    public static void main(String[] args) {
        //一开始，数组的长度为5，从键盘输入整数放到数组中，不断输入，直到输入0为止
        int[] arr = new int[5];

        Scanner input = new Scanner(System.in);

        int count = 0;//输入的数字的个数
        while(true){
            System.out.print("请输入整数：");
            int num = input.nextInt();

            if(num == 0){
                break;
            }else{
                //放到数组中
                arr[count] = num;
                count++;

                //扩容
                if(count >= arr.length){
                    //再创建一个更大的数组
//                    int[] newArr = new int[arr.length+1];//扩1个位置
//                    int[] newArr = new int[arr.length*2];//2倍扩容
//                    int[] newArr = new int[(int)(arr.length*1.5)];//1.5倍
//                    int[] newArr = new int[arr.length + arr.length/2];//1.5倍
                    int[] newArr = new int[arr.length + (arr.length>>1)];//1.5倍

                    //把数组原来的元素copy到新数组中
                    for(int i=0; i<arr.length; i++){
                        newArr[i] = arr[i];
                    }

                    //让arr指向新数组
                    arr = newArr;
                }
            }
        }


        input.close();
    }
}
