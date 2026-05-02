package day07_teacher_code.src;

public class TestArray2 {
    public static void main(String[] args) {
        int[] nums = new int[5];
        fill(nums);//给元素赋值
        System.out.println("排序之前：");
        print(nums);//打印元素值
        sort(nums);//排序
        System.out.println("排序之后：");
        print(nums);

        System.out.println("================");

        int[] arr = {2,4,5,1,2};
        System.out.println("排序之前：");
        print(arr);//打印元素值
        sort(arr);//排序
        System.out.println("排序之后：");
        print(arr);

        System.out.println("===============");
        int[] array = {4,5,6,3,1};
        print(array);
    }

    public static void fill(int[] arr){
        //给元素赋值
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int)(Math.random()*100);
        }
    }

    public static void print(int[] arr){
        //遍历数组
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void sort(int[] arr){
        //排序
        for(int i=1; i<arr.length; i++){
            for(int j=0; j<arr.length-i; j++){
                if(arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}
