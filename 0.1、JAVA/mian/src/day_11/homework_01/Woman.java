package day_11.homework_01;


public class Woman extends Person {
    public Woman(String name, int age, String job) {
        super(name, age, job);
    }

    public Woman() {
        super();
    }

    @Override
    public void eat() {
        System.out.println(getNome() + " 细嚼慢咽的吃饭");
    }

    public void makeup(){
        System.out.println(getNome() + "正在化妆");
    }
}
