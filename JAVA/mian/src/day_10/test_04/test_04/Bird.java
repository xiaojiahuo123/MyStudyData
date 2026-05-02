package day_10.test_04.test_04;

/*
类与类之间只能单继承，Bird只能有一个直接父类， Animal是Bird的亲生父亲
类与接口之间可以多实现，Bird可以同时有多个父接口，Flyable,Jumping是Bird的干爹
 */
public class Bird extends Animal implements Flyable,Jumping{
    @Override
    public void fly() {
        System.out.println("我要飞的更高！！");
    }

    @Override
    public void eat() {
        super.eat();
    }

    @Override
    public void show() {
        Flyable.super.show();
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    @Override
    public String toString() {
        return super.toString();
    }



    @Override
    public void jump() {

    }
}
