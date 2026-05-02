package day_11.test_02;

public class TestStudent {
    public static void main(String[] args) {
        Student s1 = new Student("张三",89, 23);
        Student s2 = new Student("李四",75, 24);

        int result = s1.compareTo(s2);
        if(result > 0){
            System.out.println("s1 > s2");
        }else if(result < 0){
            System.out.println("s1 < s2");
        }else{
            System.out.println("s1 == s2");
        }
    }
}
