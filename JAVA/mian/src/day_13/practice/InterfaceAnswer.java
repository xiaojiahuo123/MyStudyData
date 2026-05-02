package day_13.practice;//package day_13.practice.interface;

interface Shape {
    double area();
}
class Rectangle implements Shape {
    private double w, h;
    public Rectangle(double w, double h) { this.w = w; this.h = h; }
    public double area() { return w * h; }
}
public class InterfaceAnswer {
    // Q8 理解题答案：接口只能声明方法，不能有实现；抽象类可有方法实现和成员变量。
}
