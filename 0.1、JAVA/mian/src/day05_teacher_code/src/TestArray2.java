package day05_teacher_code.src;

public class TestArray2 {
    public static void main(String[] args) {
        /*
        用一个数组存储12个月每一个的总天数，平年。
        然后遍历输出显示平年每一个月总天数的情况
         */
        int[] daysOfMonth ;
         daysOfMonth = new int[]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        //快捷键：itar， 数组名.fori
        for (int i = 0; i < daysOfMonth.length; i++) {
            System.out.println((i+1) +"月的总天数：" + daysOfMonth[i]);
        }
    }
}
