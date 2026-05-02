package day_11.homework_02;

public class Designer extends Programmer{
    private int bonus;

    public Designer(int bonus) {
        this.bonus = bonus;
    }

    public Designer(int id, String name, int age, double salary, int bonus) {
        super(id, name, age, salary);
        this.bonus = bonus;
    }

    // 添加getBonus()方法
public int getBonus() {
    return bonus;
}

    @Override
    public String toString() {
        return super.toString().replace("程序员", "设计师") + String.format("%-8d", this.bonus);
    }
}
