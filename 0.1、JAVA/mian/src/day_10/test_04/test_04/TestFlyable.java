package day_10.test_04.test_04;

public class TestFlyable {
    public static void main(String[] args) {
//        Flyable f = new Flyable();//不能直接创建接口的对象，这一点与抽象类是一样的。
        //如何使用接口的抽象方法？
        Bird b = new Bird();//创建接口的实现类/子类对象，才能调用接口的抽象方法
        b.fly();//其实执行的是Bird中重写的fly方法

        //如何使用接口的静态方法？
        Flyable.prepare(); //接口名.静态方法

        //如何使用接口的默认方法？
        b.show();

        //只要子类重写了fly,show方法，都在执行重写后的方法体
        Plane p = new Plane();
        p.fly();
        p.show();

        //如何使用接口的常量？
        System.out.println(Flyable.SPEED);
        /*
        结论：
        使用静态的，就是类型名.静态成员
        使用非静态的，就是new对象，然后对象.非静态成员
         */
    }
}
