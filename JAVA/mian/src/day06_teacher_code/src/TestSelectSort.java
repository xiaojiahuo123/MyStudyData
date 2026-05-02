package day06_teacher_code.src;

public class TestSelectSort {
    public static void main(String[] args) {
        int[] arr = {5, 6, 3, 4, 1};

        //外循环控制几轮，n个元素，需要n-1
        //arr.length=5, i=0,1,2,3
        for(int i=0; i<arr.length-1; i++){
            //查找本轮的最小值及其下标
            int min = arr[i];//本轮第1个元素
            int index = i;

            //后面的元素与min比较
            for(int j=i+1; j<arr.length; j++){
                if(arr[j] < min){
                    min = arr[j];
                    index = j;
                }
            }

            //看一下本轮最小值在不在[i]的位置
            if(index != i){
                //交换arr[i] 与 arr[index]位置的元素
                int temp = arr[i];
                arr[i] = arr[index];
                arr[index] = temp;
            }
        }

        System.out.println("排序后：");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
    }
}
