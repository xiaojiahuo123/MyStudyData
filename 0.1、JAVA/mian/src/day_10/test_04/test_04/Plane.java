package day_10.test_04.test_04;

public class Plane implements Flyable{
    @Override
    public void fly() {
        System.out.println("飞入云霄");
    }

    @Override
    public void show() {
        System.out.println("我很酷");
    }
}
