package day07_teacher_code.src;

public class TestVarParam2 {
    public static void main(String[] args) {
        int[] arr1 = {1,2,3,4,5,6};
        System.out.println(add(arr1));

        System.out.println(add(new int[]{1,2}));
        System.out.println(add(new int[]{1}));
        System.out.println(add(new int[]{}));
    }

    //定义一个方法，用于求任意个整数的和
    public static int add(int[] nums){
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        return sum;
    }
/*    public static void test(int[] nums, int[] args){

    }*/
}
