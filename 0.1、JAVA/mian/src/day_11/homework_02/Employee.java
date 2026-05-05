package day_11.homework_02;

public class Employee {
    // 属性私有化
    private int id;
    private String name;
    private int age;
    private double salary;
    
    // 无参构造器
    public Employee() {
    }
    
    // 有参构造器
    public Employee(int id, String name, int age, double salary) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.salary = salary;
    }
    
    // get/set方法
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
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
    
    public double getSalary() {
        return salary;
    }
    
    public void setSalary(double salary) {
        this.salary = salary;
    }
    
    // say()方法：返回员工基本信息
    public String say() {
         return String.format("%-3d %-6s %-5d %-8.1f", getId(), getName(), getAge(), getSalary());
    }
    
    // 重写toString()方法，直接调用say()
    @Override
    public String toString() {
        return say();
    }
}

