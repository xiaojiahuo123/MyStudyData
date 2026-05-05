package day07_teacher_code.src;

public class TestDateTools {
    public static void main(String[] args) {
        int year = 2023;
        System.out.println(year +"是闰年吗？" + DateTools.isLeapYear(year));
        System.out.println(year  +"的总天数：" + DateTools.totalDaysOfYear(year));
    }
}
