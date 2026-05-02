package day06_teacher_code.src;

public class MyLianxi_01 {
    public static void main(String[] args) {
        int[] arr = {5, 6, 2, 7, 8, 1, 3,12};
//        查找其中的最值和对应的索引
        int max = arr[0];//假设arr[0]是最值
        int index = 0;//对应的索引是0

        for (int i = 0; i < arr.length; i++) {
            if (max < arr[i]) {
                max = arr[i];
                index = i;
            }

        }
        System.out.println("最值为 "+max + "索引是"+index);
    }
}
