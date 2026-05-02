package day_11.homework_01;


public abstract class Person {
    private String name;
    private int age;
    private String job;

    public Person(String name, int age, String job) {
        this.name = name;
        this.age = age;
        this.job = job;
    }

    public Person() {
    }

    public String getNome() {
        return name;
    }

    public void setNome(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }

    public void eat() {
        System.out.println(name + "吃饭");
    }

    public void toilet() {
        System.out.println(name + "上洗手间");
    }


    @Override
    public String toString() {
        return "Peson{" +
                "nome='" + this.name + '\'' +
                ", age=" + this.age +
                ", job='" + this.job + '\'' +
                '}';
    }
}
