package day_12.test_01;


public class TestInner {
    public static void main(String[] args) {
        // 定义一个匿名内部类继承Father
        Father f = new Father() {
            @Override
            public void method() {
                System.out.println("aaa");
            }
        };
        
        // 调用动态绑定方法，编译时看左边，运行时看右边重写的代码
        f.method();
        f.show();
        
        // 直接调用匿名内部类的方法
        new Father() {
            @Override
            public void method() {
                System.out.println("aaa");
            }
        }.method();   //这不需要实现该匿名内部类的对象（父类接收）
    }
}