package day_11.test_04;

public class Circle extends Shape{
    private double radius;//半径属性

    public Circle() {
    }

    public Circle(double radius) {
        this.radius = radius;
    }
public void eat(){
    System.out.println("Circle调用");
}
    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    @Override
    public double area(){//面积
        return Math.PI * radius * radius;
    }

    @Override
    public double perimeter(){//周长
        return 2 * Math.PI * radius;
    }

    @Override
    public String toString() {
        return "半径：" + radius + "，" + super.toString();
    }
}
