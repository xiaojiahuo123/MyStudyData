package day_11.homework_02;

public class Programmer extends Employee{//职位

    public Programmer() {
    }

    public Programmer(int id, String name, int age, double salary) {
        super(id, name, age, salary);
    }

    @Override
    public String toString() {
        return super.toString() + " 程序员       ";
    }
}
