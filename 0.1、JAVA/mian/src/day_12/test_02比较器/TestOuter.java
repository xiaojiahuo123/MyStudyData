package day_12.test_02比较器;
import day_12.test_01.Father;
public class TestOuter {
    private static int num;//成员变量，静态变量

    public static void main(String[] args) {
        String info = "尚硅谷";//局部变量
        // info = "atguigu";

        //用有名字的局部内部类继承Father类
        class Son extends Father{
            @Override
            public void method() {
                System.out.println("使用外部类的静态变量：" + num);
                System.out.println("使用外部类的方法的局部变量：" + info);
            }
        }
         // 创建局部内部类的实例并调用方法
        Son son = new Son();
        son.method(); // 调用重写的抽象方法
        son.show();   // 调用从Father类继承的非抽象方法
    }
}
