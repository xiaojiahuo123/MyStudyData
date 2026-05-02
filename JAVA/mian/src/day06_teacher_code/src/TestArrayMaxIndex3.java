package day06_teacher_code.src;

public class TestArrayMaxIndex3 {
    public static void main(String[] args) {
        int[] arr = {5, 6, 8, 7, 8, 9, 3, 9};

        /*
        方案一：（1）先找出最大值（2）再遍历数组，看哪些元素与最大值相同，打印它们的下标
         */
        int max = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > max){
                max = arr[i];
            }
        }
        System.out.println("max = " + max);

        //看哪些元素与最大值相同，打印它们的下标
        System.out.println("最大值的下标有：");
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == max){
                System.out.print("[" + i +"] ");
            }
        }
    }
}
