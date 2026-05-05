package day_10.test_02;

public class Employee {
    private String name;
    private double salary;//薪资

    public Employee() {
    }

    public Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
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


    public String getInfo() {
        return "姓名：" + name + "，薪资：" + salary;
    }
}
