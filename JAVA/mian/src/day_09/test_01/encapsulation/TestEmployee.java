package day_09.test_01.encapsulation;

public class TestEmployee {
    public static void main(String[] args) {
        Employee e1 = new Employee();//无参构造
        Employee e2 = new Employee("小孙", 30000);

        //跨类，无法直接使用对方的私有成员
        //System.out.println("姓名：" + e1.name +"，薪资：" + e1.salary);
        System.out.println("姓名：" + e1.getName() +"，薪资：" + e1.getSalary());
        System.out.println(e1.getInfo());

        System.out.println(e2.getInfo());

        //跨类，无法直接使用对方的私有成员
//        e1.name ="老马";
//        e1.salary = 18000;
        e1.setName("老马");
        e1.setSalary(18000);
        System.out.println(e1.getInfo());

    }
}
