package day07_teacher_code.src.ArrayLianxi;

import java.util.Arrays;

public class ArrayMain {
    public static void main(String[] args) {
        int[] arr = {1,2,10,4,5,10,7,8,9,10};
        System.out.println("数组最大值是："+MyDeArrays.max(arr));
        System.out.println("数组最小值是："+MyDeArrays.min(arr));
        System.out.println("复制后的新数组是："+Arrays.toString(MyDeArrays.copyOf(arr, 5)));
        System.out.println("value在arr数组中第一次出现的下标是："+MyDeArrays.indexOf(arr,5));
        System.out.println("value在arr数组中最后一次出现的下标是："+MyDeArrays.lastIndexOf(arr,2));
        System.out.println(MyDeArrays.MytoString(arr));
        MyDeArrays.sort(arr);
        System.out.println("从小到大排序后数组："+MyDeArrays.MytoString(arr));

    }
}
