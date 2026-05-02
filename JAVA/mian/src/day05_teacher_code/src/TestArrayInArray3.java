package day05_teacher_code.src;

public class TestArrayInArray3 {
    public static void main(String[] args) {
        /*
        随机产生3组[0,100)之间的整数，每一组都要5个元素
         */
        int[][] arr = new int[3][5];

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                arr[i][j] = (int)(Math.random()*100);
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
