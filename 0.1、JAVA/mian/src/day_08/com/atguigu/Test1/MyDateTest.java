package day_08.com.atguigu.Test1;

public class MyDateTest {
    public static void main(String[] args) {
        MyDate date1 = new MyDate();
        MyDate date2 = new MyDate();
        date1.MYyear=2036;
        date1.MYmonth=4;
        date1.MYday=2;

        date2.MYyear=2037;
        date2.MYmonth=7;
        date2.MYday=4;
        boolean flag = date1.isLeapYear();
       System.out.println(flag?date1.MYyear+"是闰年" : date1.MYyear + "不是闰年");

    }
}
