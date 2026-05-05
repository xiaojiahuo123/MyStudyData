package day_13.homework_02;

public class TestPerson {
    public static void main(String[] args) {
        Person person = new Person("张三",87);
        try {
            Person person1 = new Person("里斯",-6);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }


        Person person2 = new Person();
        try {
            person2.setName("解耦i大");
            person2.setLifeValue(12);
            System.out.println(person2);
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }

        try {
            person2.setLifeValue(-213);
            System.out.println(person2);
        } catch (Exception e) {
            System.out.println("出现异常");
            System.out.println(e.getMessage());
            e.printStackTrace();
        }

    }
}
