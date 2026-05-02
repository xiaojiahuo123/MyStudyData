package day_11.test_03;

public class Employee implements  Comparable{
    private String name;
    private double salary;

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

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", salary=" + salary +
                '}';
    }

    @Override
    public int compareTo(Object other) {
        //假设要按照薪资比较大小
        //this 和 other
        if( this.salary > ((Employee)other).salary){
            return 1;
        }else if(this.salary < ((Employee)other).salary){
            return -1;
        }else{
            return 0;
        }
    }
}
