package day06_teacher_code.src;

public class TestBubbleSort {
    public static void main(String[] args) {
        int[] arr = {2, 8, 6, 3, 1};

        /*
        第一轮：[0] ~ [4]
        [0] ~ [1]
        [1] ~ [2]
        [2] ~ [3]
        [3] ~ [4]
        j=0,1,2,3  j+1=1,2,3,4
         */
        for (int j = 0; j < arr.length - 1; j++) {
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }

        System.out.println("第一轮结束：");
        for (int j = 0; j < arr.length; j++) {
            System.out.print(arr[j]+" ");
        }
        System.out.println();

        /*
        第二轮：[0] ~ [3]
        [0] ~ [1]
        [1] ~ [2]
        [2] ~ [3]
        j=0,1,2  j+1=1,2,3
         */
        for (int j = 0; j < arr.length - 2; j++) {
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
        System.out.println("第二轮结束：");
        for (int j = 0; j < arr.length; j++) {
            System.out.print(arr[j]+" ");
        }
        System.out.println();

       /*
        第三轮：[0] ~ [2]
        [0] ~ [1]
        [1] ~ [2]
        j=0,1  j+1=1,2
         */
        for (int j = 0; j < arr.length - 3; j++) {
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
        System.out.println("第三轮结束：");
        for (int j = 0; j < arr.length; j++) {
            System.out.print(arr[j]+" ");
        }
        System.out.println();

        /*
        第四轮：[0] ~ [1]
        [0] ~ [1]
        j=0  j+1=1
         */
        for (int j = 0; j < arr.length - 4; j++) {
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
        System.out.println("第四轮结束：");
        for (int j = 0; j < arr.length; j++) {
            System.out.print(arr[j]+" ");
        }
        System.out.println();
    }
}
