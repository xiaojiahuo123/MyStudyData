package day_15.泛型.创建泛型类对象;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Student implements Comparable{
    private int id;
    private String name;
    private int age;

    @Override
    public int compareTo(Object o) {
        //假设按照id比较大小
        return this.id - ((Student)o).id;
    }
}
