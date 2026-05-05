package day05_teacher_code.src;

public class TestArray {
    public static void main(String[] args) {
        //组长来记录本组学员今天早上晨考的成绩，然后求它们的最大值，平均分，甚至从小到大排序....
        //第1组5个同学
/*        int s1 = 86;
        int s2 = 98;
        int s3 = 75;
        int s4 = 88;
        int s5 = 93;*/

        //scores是数组名
        int[] scores = {86, 98, 75, 88, 93};
        System.out.println("这个小组共有：" + scores.length);
        //scores[0]是元素，[0]是下标
       /* System.out.println("第1个同学的成绩：" + scores[0]);
        System.out.println("第2个同学的成绩：" + scores[1]);
        System.out.println("第3个同学的成绩：" + scores[2]);
        System.out.println("第4个同学的成绩：" + scores[3]);
        System.out.println("第5个同学的成绩：" + scores[4]);*/
//        System.out.println("第5'个同学的成绩：" + scores[5]);//会发生数组下标越界异常

        //快捷键：itar  (iterate  array)
/*        for (int i = 0; i < scores.length; i++) {
            System.out.println("第" + (i+1) + "个同学的成绩：" + scores[i]);
        }*/

        System.out.println("================");
        int i=0;
        while(i<scores.length){
            System.out.println("第" + (i+1) + "个同学的成绩：" + scores[i]);
            i++;
        }
    }
}