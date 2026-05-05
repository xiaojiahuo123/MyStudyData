package day_11.test_01;

public class Bird extends Animal implements Flyable {
    public void test(){
        System.out.println("父类的speed = " + super.speed);
        System.out.println("父接口的speed = " + Flyable.speed);//因为speed在接口中是static
    }
}
