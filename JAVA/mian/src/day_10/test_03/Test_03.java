package day_10.test_03;

public class Test_03 {
    public static void main(String[] args) {
        Circle c = new Circle(3.5);
        double area = c.area();
        System.out.println(area);
        System.out.println(c.toString());
    }
}
