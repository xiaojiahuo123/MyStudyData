package day_14.Date;

import org.junit.Test;

import java.text.SimpleDateFormat;
import java.util.Date;

public class TestFirst {
    @Test
    public void test1(){
        Date d = new Date();
        System.out.println(d);
        //Sat Dec 14 10:50:24 CST 2024

        d.setTime(5862152152L);
        System.out.println(d);
        //Tue Mar 10 04:22:32 CST 1970
    }

    @Test
    public void test2(){
        Date d = new Date();
        //2024年12月14日 10:54 周六
        SimpleDateFormat sf = new SimpleDateFormat("yyyy年MM月dd日 HH:mm E 是这一年的第D天");
        String str = sf.format(d);//把日期转为字符串
        System.out.println(str);//2024年12月14日 10:55 周六 是这一年的第349天
    }
}
