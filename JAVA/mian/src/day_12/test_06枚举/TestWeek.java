package day_12.test_06枚举;

public class TestWeek {
    public static void main(String[] args) {
//       Week w1 = new Week();//外面不能new对象
        Week w3 = Week.WEDNESDAY;//获取对象，而不是重新创建对象
        System.out.println(w3);

        String name = w3.name();
        System.out.println("name = " + name);
        int index = w3.ordinal();
        System.out.println("index = " + index);
        System.out.println("=========================");
        Week[] all = Week.values();
        for (int i = 0; i < all.length; i++) {
            System.out.println(all[i]);
        }

        System.out.println("=========================");
        //switch结构支持哪些数据类型？
        //byte,short,int,char，String，枚举
        switch (w3){
            case MONDAY -> System.out.println("最困的一天1");
            case TUESDAY -> System.out.println("最困的一天2");
            case WEDNESDAY -> System.out.println("最困的一天3");
            case THURSDAY -> System.out.println("最困的一天4");
            case FRIDAY -> System.out.println("最困的一天5");
            case SATURDAY -> System.out.println("最困的一天6");
            case SUNDAY -> System.out.println("最清醒的一天");
        }
    }
}
