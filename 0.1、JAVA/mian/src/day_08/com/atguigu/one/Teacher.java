package day_08.com.atguigu.one;

public class Teacher {
    //静态变量，静态成员变量，学校名是所有老师共享的
    public static String school;

    //实例变量，非静态成员变量，姓名、年龄、薪资是每一个老师独立的
    public String name;//姓名
    public int age;//年龄
    public double salary;//薪资
}
