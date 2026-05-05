package day06_teacher_code.src;

public class TestArrayReverse2 {
    public static void main(String[] args) {
        int[] arr = {5, 6, 7, 2, 1};
        //反转后 {1,2,7,6,5}

        System.out.print("交换之前：");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        //方案二：定义一个新数组
        int[] newArr = new int[arr.length];
        //把arr数组的元素  倒序 放到newArr中
        for (int i = 0; i < arr.length; i++) {
            newArr[arr.length-1-i] = arr[i];
        }
        arr = newArr;

        System.out.print("交换之后：");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

    }
}
