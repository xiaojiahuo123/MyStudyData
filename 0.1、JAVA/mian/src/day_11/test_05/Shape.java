package day_11.test_05;

public abstract class  Shape {
    public abstract double area();
    public abstract double perimeter();
    /*
    在抽象父类中编写这2个抽象方法的作用？
    （1）在父类中可以调用它们，如果没写，父类中就无法调用它们
    （2）在测试类中，可以通过Shape元素调用area方法
     */

    //这里重写的是Object类的toString方法
    @Override
    public String toString(){
        return "面积：" + area() +"，周长：" + perimeter();
    }

    public void eat(){
        System.out.println("Shape eat");
    }
}
