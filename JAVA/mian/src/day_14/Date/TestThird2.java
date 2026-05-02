package day_14.Date;

import org.junit.Test;
//- Period：日期间隔
//- Duration：时间间隔
import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.Period;

public class TestThird2 {
    @Test
    public void test1(){
        LocalDate today = LocalDate.now();
        LocalDate birthday = LocalDate.of(1990,8,16);

        Period p = Period.between(birthday, today );
        System.out.println(p);//P34Y3M28D
        //34年 3个月 28天
    }

    @Test
    public void test2(){
        LocalTime now = LocalTime.now();
        LocalTime xia =LocalTime.of(12,0,0);
        Duration d = Duration.between(now, xia);
        System.out.println(d);//PT28M50.8431153S
    }
}
