package day_11.test_05;



public class TestAnimal {
    public static void main(String[] args) {
        Shape d = new Rectangle();
        Shape c = new Circle();
        Shape x = new Triangle();
        look(d); //调用方法会有传参的过程  Animal animal形参 = d实参; 比较隐晦的多态引用形式
        look(c);
        look(x); // 添加这一行，使用Triangle对象
    }

    //定义一个方法，可以观察动物吃东西的行为
    public static void look(Shape shape){//形参是父类类型
        //Shape.eat();  
        shape.eat();
        // 这里直接使用了类名.方法名，这是静态方法的调用模式，非静态的方法只能通过实例化的对象调用，问题出在我使用的是Shape而不是传进来的子类实例对象shape
        //编译时shape以Shape类型呈现，即以父类类型呈现，只能调用父类有的方法
        //运行时shape执行哪个类eat方法，要看具体的实参
    }
    //可以通过重载的方式，为每一个子类都单独定义一个方法，比较麻烦，重复度高，而且后期维护的成本比较高，如果增加子类，减少子类，这些方法都要涉及到修改
/*    public static void look(Dog dog){
        dog.eat();
    }
    public static void look(Cat cat){
        cat.eat();
    }*/
}
