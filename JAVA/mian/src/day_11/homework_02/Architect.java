package day_11.homework_02;

public class Architect extends Designer{
    private int block;

    public Architect(int bonus, int block) {
        super(bonus);
        this.block = block;
    }

    public Architect(int id, String name, int age, double salary, int bonus, int block) {
        super(id, name, age, salary, bonus);
        this.block = block;
    }

    // block属性的get/set方法
    public int getBlock() {
        return block;
    }
    
    public void setBlock(int block) {
        this.block = block;
    }
    
    // 重写toString()方法，返回员工基本信息以及职位"架构师"和奖金、股票信息
    @Override
    public String toString() {
        // 获取父类的toString()信息，并添加架构师职位和股票信息
        return super.toString() + "\t\t架构师" + "\t股票数量=" + block;
    }
}
