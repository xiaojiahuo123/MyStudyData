package day_10.test_04.test_04;

public interface Flyable {
    public static final int SPEED = 100;//public static final可以省略
    public abstract void fly();

    public static void prepare(){
        System.out.println("准备起飞");
    }

    public default  void show(){
        System.out.println("我很漂亮");
    }
}
