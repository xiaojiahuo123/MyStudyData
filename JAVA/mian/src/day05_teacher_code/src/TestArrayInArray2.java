package day05_teacher_code.src;

public class TestArrayInArray2 {
    public static void main(String[] args) {
        /*
        存储：
            1 1 1 1 1
            2 2 2 2 2
            3 3 3 3 3
         */
        int[][] arr = new int[3][5];
        //[3]代表有3组，[5]代表每一组有5个元素
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                arr[i][j] = i+1;
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
