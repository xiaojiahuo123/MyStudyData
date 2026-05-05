package day_12.test_03内部类;

public class TestOuter {
    private static int a;
    private int b;
    private static int f=1;
    private int g = 1;


    class One{//非静态的成员内部类
        private static int c;
        private int d;
        private int f=2;
        private int g=2;

        public static void oneShow(){
            System.out.println("oneShow");
        }

        public void oneMethod(){
            System.out.println("a = " + a);
            System.out.println("b = " + b);
            System.out.println("自己的f = " + f);//2  就近原则
            System.out.println("外部类的f = " + TestOuter.f);//与外部类的静态变量重名，使用“外部类名.静态变量”
            System.out.println("自己的g = " + this.g);
            System.out.println("外部类的g = " + TestOuter.this.g);//与外部类的实例变量重名，使用“外部类名.this.实例变量"
            /*
            oneMethod()是一个非静态方法。调用它需要 One类的对象，
                    this代表的是One类的对象
            One是一个非静态成员内部类，使用它需要TestOuter类的对象，
                    TestOuter.this代表的是TestOuter类的对象
             */
        }
    }

    public void outShow(){
        //使用非静态内部类One类的c和d
        System.out.println("One的c = " + One.c);
        One one = new One();
        System.out.println("One的d = " + one.d);

        //使用静态内部类Two类的c和d
        System.out.println("Two的c = " + Two.c);
        Two two = new Two();
        System.out.println("Two的d = " + two.d);
    }

    public static void outMethod(){
        //使用非静态内部类One类的c和d
        System.out.println("One的c = " + One.c);
        //One one = new One();//错误，因为outMethod()是静态的，不可以使用本类TestOuter的非静态成员One
        //System.out.println("One的d = " + one.d);

        //
        System.out.println("Two的c = " + Two.c);
        Two two = new Two();
        System.out.println("Two的d = " + two.d);
    }

    static class Two{//静态的成员内部类
        private static int c;
        private int d;

        public void twoMethod(){
            System.out.println("a = " + a);
            //System.out.println("b = " + b);//错误的，静态内部类不能用外部类的非静态成员。
        }

        public static void twoShow(){
            System.out.println("twoShow");
        }
    }
}
