package day02;

public class TestLogic {
    public static void main(String[] args) {
        System.out.println(true & true);
        System.out.println(true & false);
        System.out.println(false & true);
        System.out.println(false & false);

        System.out.println("==================");
        //Alt + J，向右向下选择相同的符号或单词，修改后用Esc退出多行编辑模式
        System.out.println(true | true);
        System.out.println(true | false);
        System.out.println(false | true);
        System.out.println(false | false);

        System.out.println("==================");
        System.out.println(true ^ true);
        System.out.println(true ^ false);
        System.out.println(false ^ true);
        System.out.println(false ^ false);

        System.out.println("==================");
        //表示年龄的要求是在[18,35]
        int age = 37;// 数学中 18<=age<=35
//        System.out.println(18 <= age <= 35);
        //18 <= age 结果是 true
        //  true  <= 35 两边类型不同，无法统一

        System.out.println(18 <= age & age <= 35);//false

    }
}
