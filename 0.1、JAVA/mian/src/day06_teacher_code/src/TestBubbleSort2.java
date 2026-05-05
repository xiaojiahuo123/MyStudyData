package day06_teacher_code.src;

public class TestBubbleSort2 {
    public static void main(String[] args) {
        int[] arr = {2, 8, 6, 3, 1,7,4,3,2};

        for(int i=1; i<arr.length; i++) {//代表一共有几轮
            //为什么-i？因为每一轮比上一轮少一个元素参与
            for (int j = 0; j < arr.length - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
}
