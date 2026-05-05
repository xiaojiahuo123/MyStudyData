package day_11.homework_01;

public class Man extends Person {
    public Man(String name, int age, String job) {
        super(name, age, job);
    }

    public Man() {
        super();
    }

    @Override
    public void eat() {
        System.out.println(getNome() + " 狼吞虎咽的吃饭");
        /*
        * 子类会 自动继承 父类中所有的非私有（non-private）成员方法和成员变量。因此，
        *  Man 类的对象可以直接使用 Person 类中定义的 getNome() 方法。
        隐式的this引用
       在实例方法中调用其他实例方法时，Java会 隐式地 使用 this 关键字作为调用者。例如，
       * 在 Man 类的 eat() 方法中， getNome() 实际上等同于 this.getNome() 。这里的
       *  this 指的是当前正在执行方法的对象实例，也就是调用 eat() 方法的那个 Man 对象
        * */
    }

    public void smoke(){
        System.out.println(getNome()  +"正在抽烟");
    }
}
