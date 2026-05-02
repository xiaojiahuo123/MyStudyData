package day_12.test_03内部类;

interface Inter {
    void show();
}

class Outer {
    public static Inter method() {
        return new Inter() {
            @Override
            public void show() {
                System.out.println("HelloWorld");
            }
        };
    }
}

public class OuterDemo {
    public static void main(String[] args) {
        Outer.method().show();
    }
}