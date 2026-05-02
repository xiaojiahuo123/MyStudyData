package cms.view;

import cms.bean.Customer;
import cms.service.CustomerList ;
import cms.util.CMUtility ;

import java.util.Scanner;

public class CustomerView {
    public static void main(String[] args) {
        boolean flag = true;
        while(flag){
            System.out.println("-----------------拼电商客户管理系统-----------------");
            System.out.println("\t\t\t1 添 加 客 户");
            System.out.println("\t\t\t2 修 改 客 户");
            System.out.println("\t\t\t3 删 除 客 户");
            System.out.println("\t\t\t4 客 户 列 表");
            System.out.println("\t\t\t5 退     出");
            System.out.print("\t\t\t请选择(1-5)：");
            char select = CMUtility.readMenuSelection();
            switch (select){
                case '1' -> addCustomer();
                case '2' -> updateCustomer();
                case '3' -> deleteCustomer();
                case '4' -> listCustomer();
                case '5' -> flag = false;
            }
        }
    }

    //添加客户的信息的界面和菜单
    private static void addCustomer(){
// 代码中实际使用的是 CMUtility 类读取输入，Scanner 对象未被使用，可直接移除该代码
// 移除下面这行代码以避免资源泄漏
// Scanner sc = new Scanner(System.in);
        System.out.println("---------------------添加客户---------------------");
        System.out.print("姓名：");
        String name = CMUtility.readString(20);
        //20代表名字的长度不能超过20个字符

        System.out.print("年龄：");
        int age = CMUtility.readInt();

        System.out.print("地址：");
        String address = CMUtility.readString(11);

        System.out.print("电话：");
        String phone = CMUtility.readString(11);
        //11代表手机号码的长度不能超过11位

        System.out.print("邮箱：");
        String email = CMUtility.readString(32);

        System.out.print("性别：");
        char gender = CMUtility.readChar();
        //32代表邮箱地址的长度不能超过32个字符
        Customer customer = new Customer(name, age, address, phone,email,gender);
        //把c放到数组中
        boolean result = CustomerList.addNewCustomer(customer);
        System.out.println(result ? "添加成功" : "添加失败");

        System.out.println("---------------------添加完成---------------------");
    }

    //修改客户信息
    private static void updateCustomer(){
        System.out.println("---------------------修改客户---------------------");
        System.out.print("请选择修改客户编号(-1退出)：");
        int id = CMUtility.readInt();
        if(id == -1){
            return;//结束当前方法，回到主菜单
        }
        //修改客户，首先需要获取到原有的客户，通过方法拿到原客户的id
        Customer  customer = CustomerList.getCustomerById(id);
        //Customer customer1 = new Customer();
        if(customer == null){
            System.out.println("对应的客户不存在");
            return;
        }
        //输出客户信息
        System.out.println(customer.getInfo());
        String name = CMUtility.readString(20, customer.getName());
        //20代表名字的长度不能超过20个字符
        //这里old.getName()表示原来客户的姓名

        System.out.print("性别("+customer.getGender()+")：");
        char gender = CMUtility.readChar(customer.getGender());
        //这里old.getGender()表示原来客户的性别

        System.out.println("地址("+customer.getAddress());
        String address = CMUtility.readString(11, customer.getAddress());

        System.out.print("年龄("+customer.getAge()+")：");
        int age = CMUtility.readInt(customer.getAge());
        //这里old.getAge()表示原来客户的性别

        System.out.print("电话("+customer.getPhone()+")：");
        String phone = CMUtility.readString(11,customer.getPhone());
        //11代表手机号码的长度不能超过11位
        //这里old.getTel()表示原来客户的电话

        System.out.print("邮箱("+customer.getEmail()+")：");
        String email = CMUtility.readString(32,customer.getEmail());
        //32代表邮箱地址的长度不能超过32个字符
        //这里old.getEmail()表示原来客户的邮箱

        //为了便于把客户的信息存到数组当中，这里把上述信息放到客户对象中
        Customer c = new Customer(name,age,address,phone,email,gender);
        //把c放到数组中
        boolean result = CustomerList.replaceCustomer(id,c);
        System.out.println(result ? "修改成功" : "修改失败");

        System.out.println("---------------------修改完成---------------------");

    }

    //删除客户信息
    private static void deleteCustomer(){
        System.out.println("---------------------删除客户---------------------");
        System.out.print("请选择修改客户编号(-1退出)：");
        int id = CMUtility.readInt();
        if(id == -1){
            return;//结束当前方法，回到主菜单
        }
        boolean result = CustomerList.deleteCustomer(id);
        System.out.println(result? "删除成功!" : "删除失败");
        System.out.println("---------------------删除客户---------------------");
    }
    //输出客户列表
    private static void listCustomer(){
        System.out.println("---------------------------客户列表---------------------------");
        // 使用固定宽度格式化表头，确保对齐
        System.out.printf("%-8s%-10s%-8s%-8s%-15s%-15s%-30s\n", 
                "编号", "姓名", "性别", "年龄", "地址", "电话", "邮箱");
        System.out.println("---------------------------------------------------------------");
        Customer[] customers = CustomerList.getAllCustomers();
        if(customers == null || customers.length == 0){
            System.out.println("没有客户信息！");
        } else {
            // 遍历并打印每个客户的信息，使用相同的固定宽度格式化
            for(int i = 0; i < customers.length; i++){
                Customer c = customers[i];
                System.out.printf("%-8d%-10s%-8c%-8d%-15s%-15s%-30s\n", 
                        (i+1), c.getName(), c.getGender(), c.getAge(), 
                        c.getAddress(), c.getPhone(), c.getEmail());
            }
        }
        System.out.println("-------------------------客户列表完成-------------------------");
    }
}
