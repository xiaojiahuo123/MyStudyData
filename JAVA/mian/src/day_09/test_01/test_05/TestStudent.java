package day_09.test_01.test_05;

import java.util.Scanner;

public class TestStudent {
    public static void main(String[] args) {
        Student s1 = new Student();
        Student[] students = new Student[3];//这是创建数组对象
        System.out.println("Enter 3 students: ");//输入三个学生对象
        Scanner sc = new Scanner(System.in);

        for(int i = 0; i < students.length; i++){
            System.out.print("请输入第" + (i+1) +"个学生的姓名：");
            String name = sc.next();

            System.out.print("请输入第" + (i+1) +"个学生的成绩：");
            int score = sc.nextInt();
            //把上面输入的姓名和成绩放到学生对象中
//            students[i] = new Student(name,score);//方式一
            //方式二
            students[i] = new Student();
            students[i].setName(name);
            students[i].setScore(score);
        }
        sc.close();
//        System.out.println(students[1].getInfo());

//        遍历输出三个学生对象
        for(int i = 0; i < students.length; i++){
            System.out.println(students[i].getInfo());
        }
//        按照成绩从高到低排序
        for(int i = 1; i < students.length; i++){
            for(int j = 0; j < students.length - 1; j++){
                if(students[j].getScore() > students[j+1].getScore()){
                    Student temp = students[j];
                    students[j] = students[j+1];
                    students[j+1] = temp;
                }
            }
        }
        //        遍历输出三个学生对象
        for(int i = 0; i < students.length; i++){
            System.out.println(students[i].getScore());
        }
    }
}
