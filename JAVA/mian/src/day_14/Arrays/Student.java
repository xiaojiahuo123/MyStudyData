package day_14.Arrays;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Comparator;
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Student implements Comparable {
    //- Comparable<T> 接口 ：让类自己可以比较，需要实现 compareTo(T o) 方法
    //- Comparator<T> 接口 ：作为外部比较器，需要实现 compare(T o1, T o2) 方法
    private int id;
    private String name;
    private int score;
    private int age;

    @Override
    public int compareTo(Object o) {
        return this.id - ((Student)o).id;
    }
}
