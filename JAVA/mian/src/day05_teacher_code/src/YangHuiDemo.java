package day05_teacher_code.src;

public class YangHuiDemo {
    public static void main(String[] args) {
        //杨辉三角的特点1：第一行有 1 个元素, 第 n 行有 n 个元素
        //(1)先声明一个二维数组，行数为10行
        int[][] yangHui = new int[10][];

        //(2)分别确定10行的长度
        /*
        yangHui[0] = new int[1];//第1行的行下标是[0]，行长度是1
        yangHui[1] = new int[2];//第2行的行下标是[1]，行长度是2
        yangHui[2] = new int[3];//第3行的行下标是[2]，行长度是3
        yangHui[3] = new int[4];
        ....

        yangHui[i] = new int[i+1];
         */
        for(int i=0; i<yangHui.length; i++){
            yangHui[i] = new int[i+1];
        }

        //(3)每一行的第一个元素和最后一个元素都是 1
        /*
        每一行第1个元素：  yangHui[i][0]
        每一行最后个元素：  yangHui[i][行长度-1]  或  yangHui[i][i]
         */
        for(int i=0; i<yangHui.length; i++){
            yangHui[i][0] = 1;
            yangHui[i][i] = 1;
        }

        //(4)- 从第三行开始, 对于非第一个元素和最后一个元素的元素.
        //    yangHui[i][j] = yangHui[i-1][j-1] + yangHui[i-1][j];
        for(int i=2; i< yangHui.length; i++){
            for(int j=1; j<yangHui[i].length-1; j++) {
                yangHui[i][j] = yangHui[i - 1][j - 1] + yangHui[i - 1][j];
            }
        }

        //(5)输出
        for (int i = 0; i < yangHui.length; i++) {
            for (int j = 0; j < yangHui[i].length; j++) {
                System.out.print(yangHui[i][j]+"  ");
            }
            System.out.println();
        }

    }
}
