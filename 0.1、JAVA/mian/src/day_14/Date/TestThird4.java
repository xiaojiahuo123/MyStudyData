package day_14.Date;

import org.junit.Test;
//DateTimeFormatter：代替第1代SimpleDateFormat，对第3代日期时间对象进行格式化。
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;

public class TestThird4 {
    @Test
    public void test1(){
        LocalDateTime now = LocalDateTime.now();

        //2024年12月14日 10时54分10秒
        //DateTimeFormatter与SimpleDateFormat
        //自定义模板
        DateTimeFormatter dt = DateTimeFormatter.ofPattern("yyyy年MM月dd日 HH时mm分ss秒");//使用指定的模式创建格式化程序
        String str = dt.format(now);
        System.out.println(str);
        //2024年12月14日 11时36分00秒
    }

    @Test
    public void test2(){
        LocalDateTime now = LocalDateTime.now();

        //使用预定义模板
        DateTimeFormatter  dt = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.SHORT);
        String str = dt.format(now);
        System.out.println(str);//2024/12/14 上午11:37
    }

    @Test
    public void test3(){
        LocalDateTime now = LocalDateTime.now();

        //使用预定义模板
        DateTimeFormatter  dt = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.MEDIUM);
        String str = dt.format(now);
        System.out.println(str);//2024年12月14日 上午11:38:02
    }

    @Test
    public void test4(){
        LocalDateTime now = LocalDateTime.now();

        //使用预定义模板
        ZoneId id = ZoneId.of("Asia/Shanghai");
        DateTimeFormatter  dt = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.LONG).withZone(id);
        String str = dt.format(now);
        System.out.println(str);//2024年12月14日 CST 上午11:40:00
    }

    @Test
    public void test5(){
        LocalDateTime now = LocalDateTime.now();

        //使用预定义模板
        ZoneId id = ZoneId.of("Asia/Shanghai");
        DateTimeFormatter  dt = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.FULL).withZone(id);
        String str = dt.format(now);
        System.out.println(str);//2024年12月14日星期六 中国标准时间 上午11:40:40
    }
}
