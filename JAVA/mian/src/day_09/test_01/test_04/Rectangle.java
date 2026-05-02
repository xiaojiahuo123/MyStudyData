package day_09.test_01.test_04;

public class Rectangle {
    //属性私有化
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

    public double area(){
        return length * width;
    }
    public double perimeter(){
        return 2 * (length + width);
    }

    //接下来先忽略equals和hashCode方法
    public String toString() {
        return "Rectangle{" +
                "length=" + length +
                ", width=" + width +
                ", area = " + area() +
                ", perimeter = " + perimeter() +
                '}';
    }
}
