package day_08;

public class TestStudent {
    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student();
        Student s3 = new Student();

        System.out.println(s1);//Student@4eec7777
        System.out.println(s2);//Student@3b07d329
        System.out.println(s3);//Student@41629346
        //s1,s2,s3都是引用数据类型的变量，s1,s2,s3中都是存储对象的首地址。
        //这一点与数组一样

        int[] arr = {1,2,3,4};
        System.out.println(arr);//[I@404b9385
    }
}
