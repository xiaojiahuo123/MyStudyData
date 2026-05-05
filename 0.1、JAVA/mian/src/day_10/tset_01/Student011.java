package day_10.tset_01;

public class Student011 extends Person {
    public int score;//成绩

    public String getStudentInfo(){
        return getPersonInfo() +"，成绩：" + score;
        //间接使用父类非private的方法
    }
}
