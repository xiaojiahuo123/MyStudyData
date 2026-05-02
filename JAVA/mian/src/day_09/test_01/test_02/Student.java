package day_09.test_01.test_02;

public class Student {
    //Student 学生
    private String name;//属性私有化
    private int age;//属性私有化

    public Student() {//无参构造
    }

    public Student(String name, int age) {//有参构造
        this.name = name;
        this.age = age;
    }

    public void setAge(int age){
        if(age >= 18 && age<=35) {
            this.age = age;
        }else{
            System.out.println("年龄不合法！");
        }
    }

    public String getInfo(){
        return "姓名：" + name +"，年龄：" + age;
    }
}
