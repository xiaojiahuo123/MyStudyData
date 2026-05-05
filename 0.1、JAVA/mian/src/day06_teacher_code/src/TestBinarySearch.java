package day06_teacher_code.src;

import java.util.Scanner;

public class TestBinarySearch {
    public static void main(String[] args) {
        int[] arr = {2, 4, 6, 8, 12, 24};//数组是有序的情况下

        Scanner input = new Scanner(System.in);

        System.out.print("请输入要查找的目标值：");
        int target = input.nextInt();

        //无序数组不能用以下二分查找
        int index = -1;//初始值是-1，因为正常下标不会是-1
        int left = 0;//第一个元素的下标
        int right = arr.length - 1;//最后一个元素的下标
        //left ,right, mid，index都是下标
        while(left <= right){//当left > right就需要结束
            int mid = left + (right-left)/2; //或者  mid = (left + right)/2;
            if(target == arr[mid]){
                index = mid;
                break;
            }else if(target > arr[mid]){//去右边
                //修改左边界
                left = mid + 1;
            }else{//target < arr[mid] 去左边
                //修改右边界
                right = mid - 1;
            }
        }

        if(index == -1){
            System.out.println("不存在");
        }else{
            System.out.println("存在");
        }
        input.close();
    }
}
