package day_09.test_01.cms.atguigu.bean;

public class Customer {
    private String name;
    private char gender;
    private int age;
    private String tel;
    private String email;

    //套餐：无参构造，有参构造，get/set，toString等
    public Customer(String name, int age, String address, String phone, String email, char gender) {
    }

    public Customer(String name, char gender, int age, String tel, String email) {
        this.name = name;
        this.gender = gender;
        this.age = age;
        this.tel = tel;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public char getGender() {
        return gender;
    }

    public void setGender(char gender) {
        this.gender = gender;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String toString() {
        return name + "\t" + gender + "\t" + age + "\t" + tel + "\t" + email + "\t";
    }
}
