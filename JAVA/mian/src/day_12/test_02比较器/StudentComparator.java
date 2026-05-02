package day_12.test_02比较器;

import java.util.Comparator;

public class StudentComparator implements Comparator{
    /*    compare的调用会涉及到3个对象
    StudentComparator的对象，用于调用compare方法，
    两个对象对象，分别给o1和o2*/
    @Override
    public int compare(Object o1, Object o2) {
//        this是StudentComparator的对象
        Student s1 = (Student) o1;//向下转型
        Student s2 = (Student) o2;//向下转型
        return s1.getScore() - s2.getScore();
    }
}
