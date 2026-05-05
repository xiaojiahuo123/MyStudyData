package day07_teacher_code.src;

public class TestMethodMemory2 {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        reverse(nums);
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i]+" ");
        }
    }
    //实现了数组的反转
    public static void reverse(int[] arr){
        for(int left=0,right=arr.length-1; left<right; left++,right--){
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
        }
    }
}
