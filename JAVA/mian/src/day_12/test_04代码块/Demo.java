package day_12.test_04代码块;

public class Demo {
    static {
        System.out.println("静态代码块");
    }

    public Demo(){
        System.out.println("构造器代码");
    }

    {
        System.out.println("非静态代码块");
    }
}
