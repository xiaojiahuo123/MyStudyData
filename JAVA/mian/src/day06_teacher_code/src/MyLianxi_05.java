package day06_teacher_code.src;

public class MyLianxi_05 {
//    数组反转
public static void main(String[] args) {
    int[] arr = {5, 6, 7, 2, 1};
    //反转后 {1,2,7,6,5}

    System.out.print("交换之前：");
    for (int j : arr) {
        System.out.print(j + " ");
    }
    System.out.println();

    //方案一：对称位置的元素交换
    for(int left = 0,right = arr.length-1; left < right; left++,right--){
        //arr[left] ~ arr[right] 交换
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
    }

    System.out.print("交换之后：");
    for (int j : arr) {
        System.out.print(j + " ");
    }
    System.out.println();

  }
}
