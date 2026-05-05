package day_09.test_01.test_03;

import java.util.Objects;

public class Employee {
    private int id;
    private String name;
    private int age;
    private char gender;
    private double salary;
    private String tel;
    private String address;

    public Employee() {
        System.out.println("一个新员工入职");
    }

    public Employee(int id, String name, int age) {
        this();//调用本类的其他构造器，调用无参构造
        this.id = id;
        this.name = name;
        this.age = age;
    }

    public Employee(int id, String name, int age, char gender, double salary, String tel, String address) {
//        this.id = id;
//        this.name = name;
//        this.age = age;
        this(id, name, age);//调用本类的其他构造器，调用有参构造
        this.gender = gender;
        this.salary = salary;
        this.tel = tel;
        this.address = address;
    }

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

    public char getGender() {
        return gender;
    }

    public void setGender(char gender) {
        this.gender = gender;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    //toString()作用等价于原来的getInfo()
    //但是它比getInfo()方便，打印对象时，不用手动调用，它会自动调用
    @Override
    public String toString() {
        return "Employee{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", gender=" + gender +
                ", salary=" + salary +
                ", tel='" + tel + '\'' +
                ", address='" + address + '\'' +
                '}';
    }
//默认情况下equals等价于 ==
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Employee employee = (Employee) o;
        return id == employee.id && age == employee.age && gender == employee.gender && Double.compare(salary, employee.salary) == 0 && Objects.equals(name, employee.name) && Objects.equals(tel, employee.tel) && Objects.equals(address, employee.address);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, age, gender, salary, tel, address);
    }
}
