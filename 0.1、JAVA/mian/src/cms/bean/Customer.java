package cms.bean;

public class Customer {
    private String name;
    private int age;
    private String address;
    private String phone;
    private String email;
    private char gender;   //gender /ˈdʒendə(r)/  性别

    public Customer() {
    }

    public Customer(String name, int age, String address, String phone, String email, char gender) {
        this.name = name;
        this.age = age;
        this.address = address;
        this.phone = phone;
        this.email = email;
        this.gender = gender;
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

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public char getGender() {
        return gender;
    }

    public void setGender(char gender) {
        this.gender = gender;
    }

    public String getInfo() {
        return "Customer{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", address='" + address + '\'' +
                ", phone='" + phone + '\'' +
                ", email='" + email + '\'' +
                ", gender=" + gender +
                '}';
    }
    //输出客户列表使用
    public String getInfo(Customer c){
        return name + '\'' +
                ", " + age +
                ",'" + address + '\'' +
                ",'" + phone + '\'' +
                ", '" + email + '\'' +
                ", " + gender;
    }
}
