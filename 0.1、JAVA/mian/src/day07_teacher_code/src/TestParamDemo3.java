package day07_teacher_code.src;

public class TestParamDemo3 {
    public static void main(String[] args) {
        int[] nums = {10,20,30,40,50};
        print(nums);
        swap(nums,0,4);
        print(nums);
    }

    //功能：交换arr数组中 arr[left]与arr[right]的元素
    public static void swap(int[] arr, int left, int right){
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
    }

    public static void print(int[] arr){
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] +" ");
        }
        System.out.println();
    }
}
