package day_09.test_01.test_03;

public class TestEmployee {
    public static void main(String[] args) {
        Employee e1 = new Employee();
        Employee e2 = new Employee(2,"熊二",25);
        Employee e3 = new Employee(3,"张三",23,'男',15000,"10086","北京");


        //toString()作用等价于原来的getInfo()
        //但是它比getInfo()方便，打印对象时，不用手动调用，它会自动调用
/*        System.out.println(e1.toString());
        System.out.println(e2.toString());
        System.out.println(e3.toString());*/
        System.out.println(e1);//如果没有写toString方法，那么打印的是地址值
        System.out.println(e2);
        System.out.println(e3);

        Employee e4 = new Employee(2,"熊二",25);
        System.out.println(e2 == e4);//false
        //e2和e4是地址值，这里比较的是两个对象的地址值
        System.out.println(e2.equals(e4));//比较两个对象是否相等  false
        //默认情况下，equals等价于 ==
        //如果不想让equals方法等价于==，就必须重写
        System.out.println(e1.equals(e2));//false
    }
}
