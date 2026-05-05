package day_12.test_02比较器;

public class TestStudents {
    public static void main(String[] args) {
        Student[] arr = new Student[3];
        arr[0] = new Student(2,"熊二",89);
        arr[1] = new Student(1,"熊大",96);
        arr[2] = new Student(3,"张三",50);

        //希望按照编号从低到高排列
        System.out.println("按照编号从低到高排列：");
        MyArrays.sort(arr);

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

        //希望同一个数组，接下来按照成绩从低到高排序
        System.out.println("按照成绩从低到高排序：");
        StudentComparator sc = new StudentComparator();//有名字的普通类
        MyArrays.sort1(sc,arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
