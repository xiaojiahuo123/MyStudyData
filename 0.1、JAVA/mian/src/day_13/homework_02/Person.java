package day_13.homework_02;

public class Person {
    private String name;   //姓名
    private int lifeValue; //生命值

    public Person(String name, int lifeValue) {
        this.name = name;
        if (lifeValue < 0) {
            System.out.println("生命值不能为负数！");
            throw new RuntimeException("生命值不能为负数：" + lifeValue);
        }
        this.lifeValue = lifeValue;
    }

    public Person() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getLifeValue() {
        return lifeValue;
    }

    public void setLifeValue(int lifeValue) {
        if (lifeValue < 0) {
            System.out.println("生命值不能为负数！");
            throw new RuntimeException("生命值不能为负数：" + lifeValue);//RuntimeException - 运行时异常（非受检异常）
        }
        this.lifeValue = lifeValue;
    }

    @Override
    public String toString() {
        return super.toString();
    }
}
