package day03;

public class TestPrint2 {
    public static void main(String[] args) {
        int a = 1, b = 2;
        System.out.println(a + "," +  b);
        System.out.println("a = " + a + ",b = " + b);

        float f = 1.2F;
        double d = f;
        System.out.println(d);

        //拓展  f代表format，格式化
        System.out.printf("f=%.3f",d);

        String name = "chailinyan";
        int age = 18;
        double weight = 85.5;
        //%xx类似于占位符  不同类型的占位符不一样， 字符串%s，整数%d，小数%f
        System.out.printf("姓名:%s，年龄:%d，体重：%.1f",name, age, weight);

    }
}
