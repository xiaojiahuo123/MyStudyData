package day06_teacher_code.src;

public class TestArrayMaxIndex2 {
    public static void main(String[] args) {
        int[] arr = {5, 6, 2, 7, 8, 1, 3};

        //定义1个变量
        int index = 0; //index是下标，最大值的下班
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > arr[index]){
                index = i;
            }
        }
        System.out.println("max = " + arr[index]);
        System.out.println("index = [" + index +"]");
        System.out.println("第" + (index+1) +"个最大");
    }
}
