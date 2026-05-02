package day_14.Arrays;

import org.junit.Test;

import java.util.Arrays;

public class TestSystemArraycopy {
    @Test
    public void test1(){
        int[] nums = {1,2,3,4,5};
        int[] arr = new int[10];

        //想要实现将nums的5个元素，复制到arr数组中 arr[0]~arr[4]
        System.arraycopy(nums, 0, arr, 0, 5);
        /*
        从原数组复制元素到目标数组
        第1个参数：原数组
        第2个参数：要复制的元素的最左边的下标
        第3个参数：目标数组
        第4个参数：目标数组要存储新元素最左边的下标
        第5个参数：一共几个元素
         */
        System.out.println(Arrays.toString(arr));
    }

    @Test
    public void test2(){
        int[] nums = {1,2,3,4,5};
        int[] arr = new int[10];

        //想要实现将nums的5个元素，复制到arr数组中 arr[3]~arr[7]
        System.arraycopy(nums, 0, arr, 3, 5);
        /*
        从原数组复制元素到目标数组
        第1个参数：原数组
        第2个参数：要复制的元素的最左边的下标
        第3个参数：目标数组
        第4个参数：目标数组要存储新元素最左边的下标
        第5个参数：一共几个元素
         */
        System.out.println(Arrays.toString(arr));
    }

    @Test
    public void test3(){
        int[] nums = {1,2,3,4,5};

        //将元素2删除，即把nums[1]位置的元素删除
        //实现的思路：把nums[2],nums[3],nums[4]元素往左复制
        //          nums[2] -> nums[1]
        //          nums[3] -> nums[2]
        //          nums[4] -> nums[3]
        System.arraycopy(nums, 2, nums, 1, 3);
        System.out.println(Arrays.toString(nums));//[1, 3, 4, 5, 5]

//        nums[nums.length-1] = 0;
//        System.out.println(Arrays.toString(nums));//[1, 3, 4, 5, 0]
        nums = Arrays.copyOf(nums, nums.length-1);
        System.out.println(Arrays.toString(nums));
    }

    @Test
    public void test4(){
        int[] nums = {1,2,3,4,5};
        //在nums[1]位置插入6元素 ，使得数组变为 {1,6,2,3,4,5}

        //扩容
        nums = Arrays.copyOf(nums, nums.length+1);
        System.out.println(Arrays.toString(nums));//[1, 2, 3, 4, 5, 0]

        //将nums[1]~nums[4]元素往右复制到nums[2]~nums[5]
        System.arraycopy(nums, 1, nums, 2, 4);
        System.out.println(Arrays.toString(nums));

        nums[1] = 6;
        System.out.println(Arrays.toString(nums));
    }
}
