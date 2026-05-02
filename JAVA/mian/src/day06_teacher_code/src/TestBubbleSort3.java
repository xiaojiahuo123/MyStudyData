package day06_teacher_code.src;

public class TestBubbleSort3 {
    public static void main(String[] args) {
        int[] arr = {1,2,3,5,4};

        /*
        思考：如果提前已经排好序了，没必要非得执行n-1轮？
        换一个问题：如何通过代码检测数组已经排序好？
         */

        for(int i=1; i<arr.length; i++) {
            boolean flag = true;//true代表已经排好序了
            for (int j = 0; j < arr.length - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;

                    flag = false;//可能还未排好序
                }
            }

            if(flag){
                break;//结束外循环
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
}
