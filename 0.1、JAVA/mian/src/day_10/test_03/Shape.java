package day_10.test_03;

public abstract class Shape {
    private String name;

    //没有方法体的Java方法，需要加abstract，表示它是一个抽象方法
    public abstract double area();
    public abstract double perimeter();

    //此时构造器是给子孙后代用的，不是自己用的
    public Shape() {
    }

    public Shape(String name) {
        this.name = name;
    }

    public String toString(){
        return "面积：" + area() +"，周长：" + perimeter();
    }
}
