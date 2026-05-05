package day07_teacher_code.src;

public class TestParamDemo4_2 {
    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5};

        print(nums);//1,2,3,4,5
        nums = change(nums);//接收新数组的首地址
        print(nums);
        //100,2,3,4,5
    }

    public static int[] change(int[] arr){
        arr[0] = 100;
        arr = new int[arr.length+1];//让形参指向新的数组对象，接下来arr的任何操作与实参无关了
        arr[0] = 200;
        return arr;//返回新的数组的首地址
    }

    public static void print(int[] arr){
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] +" ");
        }
        System.out.println();
    }
}
