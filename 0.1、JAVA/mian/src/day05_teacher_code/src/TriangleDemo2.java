package day05_teacher_code.src;

/*
用二维数组完成如下数字图形的存储和打印
10
10 20
10 20 30
10 20 30 40
 */
public class TriangleDemo2 {
    public static void main(String[] args) {
        //(1)先确定行数
        int[][] arr = new int[4][];//每一行几个元素此时不知道

        //(2)再确定每一行的元素个数
       /* arr[0] = new int[1];
        arr[1] = new int[2];
        arr[2] = new int[3];
        arr[3] = new int[4];*/
/*        for(int i=0; i<arr.length; i++){
            arr[i] = new int[i+1];
        }*/

        /*arr[0][0] = 10;

        arr[1][0] = 10;
        arr[1][1] = 20;

        arr[2][0]= 10;
        arr[2][1]= 20;
        arr[2][2]= 30;

        arr[3][0] = 10;
        arr[3][1] = 20;
        arr[3][2] = 30;
        arr[3][3] = 40;*/
/*        for(int i=0; i<arr.length; i++){
            for(int j=0; j<arr[i].length; j++){
                arr[i][j] = 10 * (j+1);
            }
        }

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j]+"\t");
            }
            System.out.println();
        }*/

        for (int i = 0; i < arr.length; i++) {
            arr[i] = new int[i+1];
            for (int j = 0; j < arr[i].length; j++) {
                arr[i][j] = 10 * (j+1);
                System.out.print(arr[i][j]+"\t");
            }
            System.out.println();
        }
    }
}
