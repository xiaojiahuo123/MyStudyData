package day05_teacher_code.src;

public class ArrayExercise1_2 {
    public static void main(String[] args) {
        //随机产生5个[0,100)的偶数放到数组中 ，并遍历输出
        //(1)先声明数组，类型是int[]，长度是5
        int[] arr = new int[5];

        //(2)随机产生5个[0,100)的整数，然后是偶数再放到数组中
        for (int i = 0; i < arr.length; ) {
            int num = (int)(Math.random()*100);
            if(num % 2 == 0){
                arr[i] = num;
                System.out.print(arr[i] +" ");
                i++;
            }
        }
    }
}
