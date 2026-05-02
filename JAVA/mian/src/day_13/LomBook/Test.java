package day_13.LomBook;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor //生成无参构造
@AllArgsConstructor //生成全参构造
public class Test {
    public String name;
    private int age;
}
