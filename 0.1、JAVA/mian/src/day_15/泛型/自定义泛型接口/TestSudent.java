package day_15.泛型.自定义泛型接口;

public class TestSudent {
    public static void main(String[] args) {
        Student<Integer> s1 = new Student<>("张三",45,67);
        
        // 创建String类型的泛型对象
        Student<String> s2 = new Student<>("李四","优秀","及格");
        
        // 创建Double类型的泛型对象
        Student<Double> s3 = new Student<>("王五",98.5,67.5);
        
        // 再创建一个Double类型的泛型对象
        Student<Double> s4 = new Student<>("赵六",88.0,77.0);


    }
}
