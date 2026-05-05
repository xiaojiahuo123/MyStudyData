package day05_teacher_code.src;

public class TestArrayArithmeticDemo {
    public static void main(String[] args) {
        /*
        需求：随机产生10个[0,100)的整数，打印显示它们
        然后求它们的总和和平均值
         */
        //(1)声明一个int[]类型的数组，长度为10
        int[] arr = new int[10];

        //(2)随机产生10个[0,100)的整数，放到数组中，打印显示它们
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int)(Math.random()*100);
            System.out.print(arr[i]+" ");
        }
        System.out.println();

        //（3）求它们的总和与平均值
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        System.out.println("总和：" + sum);
        System.out.println("平均值：" + (double)sum / arr.length);
    }
}
