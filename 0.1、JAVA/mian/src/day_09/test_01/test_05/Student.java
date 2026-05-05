package day_09.test_01.test_05;

public class Student {
    //score  分数  /skɔː(r)/
    private String name;
    private int score;
//无参构造
    public Student() {
    }
//有参构造
    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }


    public String getInfo() {
        return "Student{" +
                "学生姓名'" + name + '\'' +
                ", 成绩为" + score +
                '}';
    }
}
