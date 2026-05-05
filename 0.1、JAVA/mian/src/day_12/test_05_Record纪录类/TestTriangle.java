package day_12.test_05_Record纪录类;

public class TestTriangle {
    public static void main(String[] args) {
        Triangle t1 = new Triangle(3,4,5);
        Triangle t2 = new Triangle(3,4,5);
        System.out.println(t1);
        // System.out.println(t1.toString());
        System.out.println(t2);
        //打印对象，会自动调用对象的toString()
        //如果没有重写toString，默认出来的 像地址值的东西
        System.out.println(t1.equals(t2));
        //如果equals没有重写，默认比较的是对象的首地址

        System.out.println("单独获取a边的值：" + t1.a());
    }
}
