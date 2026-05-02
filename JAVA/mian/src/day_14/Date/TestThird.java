package day_14.Date;

import org.junit.Test;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.Month;

public class TestThird {
    @Test
    public void test1(){
        //今天的日期
        LocalDate today = LocalDate.now();
        System.out.println(today);
        //2024-12-14
    }

    @Test
    public void test2(){
        //现在时间
        LocalTime now = LocalTime.now();
        System.out.println(now);
        //11:19:23.539160300
    }

    @Test
    public void test3(){
        LocalDateTime dateTime = LocalDateTime.now();
        System.out.println(dateTime);
        //2024-12-14T11:19:57.219802900
    }

    @Test
    public void test4(){
        //开班日期
        LocalDate kai = LocalDate.of(2024,11,25);
        System.out.println(kai);
    }

    @Test
    public void test5(){
        LocalDate today = LocalDate.now();
        int year = today.getYear();
        Month month = today.getMonth();
        int monthValue = today.getMonthValue();
        int day = today.getDayOfMonth();
    }

    @Test
    public void test6(){
        //开班日期
        LocalDate kai = LocalDate.of(2024,11,25);

        //过195天是哪一天
        LocalDate bi = kai.plusDays(195);
        System.out.println(kai);//2024-11-25 对象不可变
        System.out.println(bi);//2025-06-08
    }

    @Test
    public void test7(){
        //开班日期
        LocalDate kai = LocalDate.of(2024,11,25);

        //100天之前
        LocalDate before = kai.minusDays(100);
        System.out.println(before);//2024-08-17
    }
}
