package day_13.LomBook;

public class Mytest {
    public static void main(String[] args) {
        Test t = new Test("打",1223);
        System.out.println(t);

        Test e2 = new Test();
        System.out.println(e2);
e2.setName("张三");
        e2.setAge(15000);
        System.out.println(e2.getName());

        System.out.println(t.equals(e2));
    }
}
