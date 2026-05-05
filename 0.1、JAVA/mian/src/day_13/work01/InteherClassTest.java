package day_13.work01;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.junit.Test;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Getter
public class InteherClassTest {
    public Integer i;
@Test
    public void test01(){
        try {
            if (i % 2 == 0){
                System.out.println("输入的数是整数");
            }else {
                System.out.println("不是整数");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }
}
