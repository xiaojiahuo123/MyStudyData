package day_11.test_06;

public class Zi extends Fu {
    private int a = 2;
    private int b = 2;
    protected int d = 2;

    @Override
    public int getA() {
        return a;
    }

    public void test(){
        System.out.println("子类a = " + a);
//        System.out.println("父类a = " + super.a);//错误的，父类的a是private
        System.out.println("子类的b = " + b);
//        System.out.println("父类的c = " + c);//无法访问

        System.out.println("子类的d = " + d);
        System.out.println("子类的d = " + this.d);
        System.out.println("父类的d = " + super.d);

        System.out.println("父类的e = " + e);
        System.out.println("父类的e = " + this.e);
        System.out.println("父类的e = " + super.e);

        System.out.println("子类的a = " + getA());//子类有自己的getA()
        System.out.println("父类的a = " + super.getA());//子类有自己的getA()
        System.out.println("父类的b = " + getB());
    }

    public void test(int d){
        System.out.println("参数d = " + d);
        System.out.println("子类的d = " + this.d);
        System.out.println("父类的d = " + super.d);
    }
}
