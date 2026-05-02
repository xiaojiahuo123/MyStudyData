package day_12.homework1;

public class TestObject {
    public static void main(String[] args) {
        new Object(){
            public void print() {
                System.out.println("Hello World");
            }
        }.print();
    }
}
