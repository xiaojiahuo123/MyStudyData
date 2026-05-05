package day07_teacher_code.src;

public class TestVarParam {
    public static void main(String[] args) {
        System.out.println(add(1,2,3,4,5,6));
        System.out.println(add(1,2));
        System.out.println(add(1));
        System.out.println(add());

        int[] arr = {10,20,30,40,50};
        System.out.println(add(arr));
    }

    //定义一个方法，用于求任意个整数的和
    public static int add(int... nums){
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        return sum;
    }

/*    public static void test(int... nums, int... args){//错误，一个方法不能有2个可变参数

    }*/
}
