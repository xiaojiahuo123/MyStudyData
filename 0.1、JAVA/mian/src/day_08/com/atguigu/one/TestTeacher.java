package day_08.com.atguigu.one;

public class TestTeacher {
    public static void main(String[] args) {
//        System.out.println("姓名：" + name);//错误，name在Teacher类中
        // System.out.println("姓名：" + Teacher.name);//错误，因为name没有static

        System.out.println("学校：" + Teacher.school);//null

        Teacher t1 = new Teacher();//创建对象，创建实例
        System.out.println("t1的姓名：" + t1.name);//null
        System.out.println("t1的年龄：" + t1.age);//0
        System.out.println("t1的薪资：" + t1.salary);//0.0

//        int a;//局部变量
//        System.out.println("a = " + a);//报错，因为a没有初始化

        System.out.println("赋值之前：");

        Teacher.school = "尚大";
        t1.name = "张三";
        t1.age = 23;
        t1.salary = 16500;

        Teacher t2 = new Teacher();
        t2.school = "尚硅谷";//推荐用 Teacher.school = "尚硅谷";

        System.out.println("t1的学校：" + t1.school);//推荐用 Teacher.school
        System.out.println("t1的姓名：" + t1.name);
        System.out.println("t1的年龄：" + t1.age);
        System.out.println("t1的薪资：" + t1.salary);

        System.out.println("t2的学校：" + t2.school);//推荐用 Teacher.school
        System.out.println("t2的姓名：" + t2.name);
        System.out.println("t2的年龄：" + t2.age);
        System.out.println("t2的薪资：" + t2.salary);

    }
}
