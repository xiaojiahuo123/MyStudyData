package day05_teacher_code.src;

public class TestArrayInArray {
    public static void main(String[] args) {
        /*
        存储咱们班3组同学的成绩
         */
        int[][] scores = {{89, 85, 86, 75}, {99, 98, 93, 92, 91}, {63, 76}};
        /*
        scores[0] 是一个一维数组  {89, 85, 86, 75}
        scores[1] 也是一个一维数组  {99, 98, 93, 92, 91}
        scores[2] 也是一个一维数组  {63, 76}

          */
        //System.out.println(scores);//[[I@776ec8df，它是二维数组的首地址，有两个[

        //遍历二维数组
/*        for (int i = 0; i < scores.length; i++) {
            System.out.println(scores[i]);//[I@4eec7777 它是一维数组的首地址，有一个[
        }*/

        /*
        scores.length 是3，代表有3组，把每一组看成一个整体，二维数组也相当于是一维数组，只不过此时它的元素也是数组。
        scores[0].length 是4
        scores[1].length 是5
        scores[2].length 是2
         */
        for (int i = 0; i < scores.length; i++) {
            //scores[i]是一维数组，它的长度是scores[i].length
            for(int j=0; j<scores[i].length; j++){
                System.out.print(scores[i][j]+" ");
            }
            System.out.println();
        }
    }
}
