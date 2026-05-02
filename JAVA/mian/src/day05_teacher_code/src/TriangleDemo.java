package day05_teacher_code.src;

/*
用二维数组完成如下数字图形的存储和打印
10
10 20
10 20 30
10 20 30 40
 */
public class TriangleDemo {
    public static void main(String[] args) {
/*        int[][] arr = {
                {10},
                {10,20},
                {10,20,30},
                {10,20,30,40}
        };*/

        int[][] arr = {{10}, {10,20}, {10,20,30}, {10,20,30,40}};

        //上面的代码，总行数、以及每一行的元素个数、以及每一行的每一个元素都是确定的
        //在.java文件 -> .class文件的过程中 已经确定了，
        //通俗的讲：写死了
        //称为静态初始化，下面只要遍历即可
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j]+"\t");
            }
            System.out.println();
        }

    }
}
