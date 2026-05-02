package day_11.test_02;

public class Student implements Comparable{
    private String name;
    private int age;
    private int score;

    public Student( ) {
    }

    public Student(String name, int age, int score) {
        this.name = name;
        this.age = age;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", score=" + score +
                '}';
    }

    @Override
    public int compareTo(Object other) {//比较器

              /*
        1、这里有2个对象在比较大小？
        this 和 other 两个对象比较大小

        2、怎么比较大小？根据需求来定
        假设，这里按照成绩比较大小
        this.score 与 other.score
         */
        return this.score - ((Student)other).score;//这里的((Student)other)是对other进行强制类型转换为Student对象
    }
}
