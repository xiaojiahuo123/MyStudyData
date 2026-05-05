package day_14.Arrays;

public class MyArrays {//模仿Arrays数组工具类
    public static int[] copyOf(int[] arr, int newLength){
        //第一步：创建新数组
        int[] newArr = new int[newLength];

        //第二步：复制元素
/*        for (int i = 0; i < newArr.length && i<arr.length; i++) {
            newArr[i] = arr[i];
        }*/
        for (int i = 0; i < Math.min(arr.length,newArr.length); i++) {
            newArr[i] = arr[i];
        }

        //第三步：返回新数组
        return newArr;
    }
}
