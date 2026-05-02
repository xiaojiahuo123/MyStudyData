package day06_teacher_code.src;

public class TestArrayDelete {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};

        //删除元素20，并且要保证剩下的元素仍然是连续存储
        //(1)把[1]位置及其后面的元素往前移动
        /*
        [2] -> [1]
        [3] -> [2]
        [4] -> [3]
         */
        //arr.length=5,  i=1,2,3
        for(int i=1; i<arr.length-1; i++){
//            arr[前面] = arr[后面];
            arr[i] = arr[i+1];
        }

        //(2)把末尾位置置0
        arr[arr.length-1] = 0;

        System.out.println("删除20元素后：");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }

    }
}
