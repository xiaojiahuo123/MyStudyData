package day_09.test_01.encapsulation;

public class Teacher {
    private static String company;
    private String name;
    private double salary;
    private boolean marry;

    //用快捷键生成构造器、get/set方法  Alt + Insert

    public Teacher() {
    }

    public Teacher(String name, double salary, boolean marry) {
        this.name = name;
        this.salary = salary;
        this.marry = marry;
    }

    public static String getCompany() {
        return company;
    }

    public static void setCompany(String company) {
        Teacher.company = company;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public boolean isMarry() {
        return marry;
    }

    public void setMarry(boolean marry) {
        this.marry = marry;
    }

    public String getInfo() {
        return "Teacher{" +
                "name='" + name + '\'' +
                ", salary=" + salary +
                ", marry=" + marry +
                '}';
    }
}
