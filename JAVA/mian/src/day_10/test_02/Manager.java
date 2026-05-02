package day_10.test_02;

public class Manager extends Employee{
    private double bonus;//奖金

    public Manager() {
    }

    public Manager(String name, double salary, double bonus) {
        super(name, salary);
        this.bonus = bonus;
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public String  getInfo(){
        // return "姓名：" + getName() + "，薪资：" + getSalary() + "，奖金：" + bonus;
        return super.getInfo() + "，奖金：" + bonus;
        //通过super关键字，调用父类被重写的方法
    }
}
