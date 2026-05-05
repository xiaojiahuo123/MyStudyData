package day_11.test_04;

public class Rectangle extends Shape {
    private double length;
    private double width;

    public Rectangle() {
    }

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    //重写了抽象父类的两个抽象方法
    @Override
    public double area(){
        return length * width;
    }

    @Override
    public double perimeter(){
        return (length + width) * 2;
    }

    @Override
    public String toString() {
        return "长：" + length + ", 宽：" + width + "，" + super.toString();
    }
}
