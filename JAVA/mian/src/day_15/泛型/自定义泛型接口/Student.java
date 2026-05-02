package day_15.泛型.自定义泛型接口;

public class Student<T>{
    private String name;
    private T score;
    private T info;

    public Student(String name, T score, T info) {
        this.name = name;
        this.score = score;
        this.info = info;
    }

    public T getScore(){
        return score;
    }

    public T getInfo(){
        return info;
    }

    @Override
    public String toString() {
        return
                '{' + "name='" + name + '\'' +
                ", score=" + score +
                ", info=" + info +
                '}';
    }
}
