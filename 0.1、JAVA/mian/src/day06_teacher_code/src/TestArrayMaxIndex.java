package day06_teacher_code.src;

public class TestArrayMaxIndex {
    public static void main(String[] args) {
        int[] arr = {5, 6, 2, 7, 8, 1, 3};

        //定义两个变量，一个代表最大值，一个代表最大值的下标
        int max = arr[0];//max是最大值
        int index = 0; //index是下标
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > max){
                max = arr[i];
                index = i;
            }
        }
        System.out.println("max = " + max);
        System.out.println("index = [" + index +"]");
        System.out.println("第" + (index+1) +"个最大");
    }
}
