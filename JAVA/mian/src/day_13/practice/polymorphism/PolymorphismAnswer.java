package day_13.practice.polymorphism;

class Person {
    public void sayHello() { System.out.println("我是人"); }
}
class Student extends Person {
    @Override
    public void sayHello() { System.out.println("我是学生"); }
}
public class PolymorphismAnswer {
    public static void main(String[] args) {
        Person p = new Student();
        p.sayHello(); // 输出：我是学生
    }
    // Q6 理解题答案：多态前提：有继承/实现关系，有方法重写，父类引用指向子类对象。
}
