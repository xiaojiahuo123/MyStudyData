package day_09.test_01.encapsulation;

public class Employee {
    private static String company;
    private String name;
    private double salary;
    private boolean marry;

    public Employee() {
    }

    public Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    //set方法的作用：供类外面，修饰某个/某些属性的值
    public void setName(String name){
        this.name = name;
    }
    public void setSalary(double salary){
        this.salary = salary;
    }
    public void setMarry(boolean marry){
        this.marry = marry;
    }
    public static void setCompany(String company){
        Employee.company = company;
    }
    //这种set一般是可选
    public void setInfo(String name, double salary){
        this.name = name;
        this.salary = salary;
    }

    //get方法的作用：供类外面，获取某个/某些属性的值
    public String getName(){
        return name;
    }
    public double getSalary(){
        return salary;
    }
    public boolean isMarry(){
        return marry;
    }
    public static String getCompany(){
        return company;
    }
    public String getInfo(){
        return "姓名：" + name +"，薪资：" + salary;
    }
}
