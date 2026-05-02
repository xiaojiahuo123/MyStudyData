package day_10.tset_01;

public class Student extends Person {
    public int score;//成绩

    public String getStudentInfo(){
        return "姓名：" + name + "，年龄：" + age +"，成绩：" + score;
        //直接使用父类非private的属性
    }
}
