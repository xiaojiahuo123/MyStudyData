import java.util.Random;

public class RandomDemo {
    public static void main(String[] args) {
        double random = Math.random();
        double random1 = Math.random() * 100;
        System.out.println(random1);
        System.out.println(random);
        int b = (int)random1;  //这是强制转换数据类型，将random转换为int数据
        System.out.println("b = " + b);

        Random random2 = new Random();
        int b1 = random2.nextInt(0,100);
        System.out.println("b1 = " + b1);
    }
}
