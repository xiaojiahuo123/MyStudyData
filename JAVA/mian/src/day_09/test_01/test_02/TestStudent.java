package day_09.test_01.test_02;

public class TestStudent {
    public static void main(String[] args) {
        //调用Student类的无参构造创建Student对象
        Student s1 = new Student();
        System.out.println(s1.getInfo());

        //调用Student类的有参构造创建Student对象
        Student s2 = new Student("张三",23);
        System.out.println(s2.getInfo());

        //s2.age = -18;//不安全
        s2.setAge(-18);//安全
        System.out.println(s2.getInfo());

        s2.setAge(30);//安全
        System.out.println(s2.getInfo());
    }
}
