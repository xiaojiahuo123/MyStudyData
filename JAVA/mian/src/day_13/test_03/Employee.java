package day_13.test_03;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data //自动生成get/set，equals和hashCode，toString等方法
@NoArgsConstructor //生成无参构造
@AllArgsConstructor //生成全参构造，为所有实例变量初始化的构造器
public class Employee implements Comparable{
    private int id;
    private String name;
    private double salary;
    private int age;

    @Override
    public int compareTo(Object o) {
        return this.id - ((Employee)o).id;
    }
}
