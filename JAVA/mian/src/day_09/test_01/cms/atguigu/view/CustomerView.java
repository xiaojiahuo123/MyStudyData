package day_09.test_01.cms.atguigu.view;
import day_09.test_01.cms.atguigu.bean.Customer;
import day_09.test_01.cms.atguigu.service.CustomerList;
import day_09.test_01.cms.atguigu.util.CMUtility;

//收拢所有方法的快捷键：Ctrl + Shift + -
public class CustomerView {
    //主菜单
    public static void main(String[] args) {
        boolean flag = true;

        //添加一下模拟数据，便于测试
        Customer c1 = new Customer("张三",'男',23,"10086","zhang@123.com");
        Customer c2 = new Customer("李四",'男',24,"10010","lisi@123.com");
        CustomerList.addNewCustomer(c1);
        CustomerList.addNewCustomer(c2);

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

    //客户列表功能
    private static void listCustomer() {
        System.out.println("---------------------------客户列表---------------------------");
        System.out.println("编号\t姓名\t性别\t年龄\t电话\t\t邮箱");
        //调用CustomerList类的一个方法，来获取数组中所有的客户对象
        Customer[] all = CustomerList.getAllCustomers();
        for (int i = 0; i < all.length; i++) {
            System.out.println((i+1) +"\t" + all[i]);
            //打印对象，默认会调用对象的toString方法，这里all[i].toString，会找Customer的toString()
            //因为all[i]是Customer类型
        }

        System.out.println("---------------------------客户列表完成---------------------------");
    }

    //删除功能
    private static void deleteCustomer() {
        System.out.println("---------------------删除客户---------------------");
        System.out.print("请选择待删除客户编号(-1退出)：");
        int id = CMUtility.readInt();
        if(id == -1){
            return;//结束当前方法，回到主菜单
        }
        System.out.print("确认是否删除(Y/N)：");
        char confirm = CMUtility.readConfirmSelection();
        if(confirm == 'y' || confirm== 'Y'){
            //调用CustomerList类中某个方法，完成删除编号为id的客户对象
            boolean result = CustomerList.removeCustomer(id);
            System.out.println(result ? "删除成功" : "删除失败");
        }

        System.out.println("---------------------删除完成---------------------");

    }

    //修改功能
    private static void updateCustomer() {
        System.out.println("---------------------修改客户---------------------");
        System.out.print("请选择修改客户编号(-1退出)：");
        int id = CMUtility.readInt();
        if(id == -1){
            return;//结束当前方法，回到主菜单
        }

        //调用CustomerList类的某个方法，拿到旧客户对象，根据id来查询这个客户对象
        Customer old = CustomerList.getCustomerById(id);
        if(old == null){
            System.out.println(id +"对应的客户不存在！");
            return;
        }

        System.out.print("姓名("+old.getName()+")：");
        String name = CMUtility.readString(20, old.getName());
        //20代表名字的长度不能超过20个字符
        //这里old.getName()表示原来客户的姓名

        System.out.print("性别("+old.getGender()+")：");
        char gender = CMUtility.readChar(old.getGender());
        //这里old.getGender()表示原来客户的性别

        System.out.print("年龄("+old.getAge()+")：");
        int age = CMUtility.readInt(old.getAge());
        //这里old.getAge()表示原来客户的性别

        System.out.print("电话("+old.getTel()+")：");
        String tel = CMUtility.readString(11,old.getTel());
        //11代表手机号码的长度不能超过11位
        //这里old.getTel()表示原来客户的电话

        System.out.print("邮箱("+old.getEmail()+")：");
        String email = CMUtility.readString(32,old.getEmail());
        //32代表邮箱地址的长度不能超过32个字符
        //这里old.getEmail()表示原来客户的邮箱

        //为了便于把客户的信息存到数组当中，这里把上述信息放到客户对象中
        Customer c = new Customer(name,gender,age,tel,email);
        //把c放到数组中
        boolean result = CustomerList.replaceCustomer(id,c);
        System.out.println(result ? "修改成功" : "修改失败");

        System.out.println("---------------------修改完成---------------------");
    }

    //添加客户的信息的界面和菜单
    private static void addCustomer() {
        System.out.println("---------------------添加客户---------------------");
        System.out.print("姓名：");
        String name = CMUtility.readString(20);
        //20代表名字的长度不能超过20个字符

        System.out.print("性别：");
        char gender = CMUtility.readChar();

        System.out.print("年龄：");
        int age = CMUtility.readInt();

        System.out.print("电话：");
        String tel = CMUtility.readString(11);
        //11代表手机号码的长度不能超过11位

        System.out.print("邮箱：");
        String email = CMUtility.readString(32);
        //32代表邮箱地址的长度不能超过32个字符

        //为了便于把客户的信息存到数组当中，这里把上述信息放到客户对象中
        Customer c = new Customer(name,gender,age,tel,email);
        //把c放到数组中
        boolean result = CustomerList.addNewCustomer(c);
        System.out.println(result ? "添加成功" : "添加失败");

        System.out.println("---------------------添加完成---------------------");
    }
}
