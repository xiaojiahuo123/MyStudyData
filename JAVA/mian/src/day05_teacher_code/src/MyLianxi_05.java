package day05_teacher_code.src;

public class MyLianxi_05 {
    public static void main(String[] args) {
        int[][] arr = new int[10][];

        for(int i=0; i<arr.length; i++){
            arr[i] = new int[i+1];
        }

        /*
        每一行第1个元素：  yangHui[i][0]
        每一行最后个元素：  yangHui[i][行长度-1]  或  yangHui[i][i]
         */
        for(int i=0; i<arr.length; i++){
            arr[i][0] = 1;
            arr[i][i] = 1;
        }


        for(int i=2; i< arr.length; i++){
            for(int j=1; j<arr[i].length-1; j++) {
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
            }
        }

        //(5)输出
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j]+"  ");
            }
            System.out.println();
        }
    }
}
