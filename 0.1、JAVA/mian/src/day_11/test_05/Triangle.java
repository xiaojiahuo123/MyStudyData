package day_11.test_05;

public class Triangle extends Shape {
    private double a;
    private double b;
    private double c;

    public Triangle() {
    }

    public Triangle(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getA() {
        return a;
    }

    public void setA(double a) {
        this.a = a;
    }

    public double getB() {
        return b;
    }

    public void setB(double b) {
        this.b = b;
    }

    public double getC() {
        return c;
    }

    public void setC(double c) {
        this.c = c;
    }
    //重写父类抽象方法的快捷键：Ctrl + O 或 Ctrl + I
    //Ctrl + O可以重写父类抽象的和非抽象的方法
//    Ctrl + I 重写父类或父接口的抽象方法

    @Override
    public double area() {
        double p = (a+b+c)/2;
        return Math.sqrt(p * (p-a) * (p-b) * (p-c));
    }

    @Override
    public double perimeter() {
        return a + b + c;
    }

    @Override
    public String toString() {
        return "边长：" + a +
                "," + b +
                "," + c
                + "，" + super.toString();
    }
}
