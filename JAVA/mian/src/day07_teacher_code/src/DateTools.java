package day07_teacher_code.src;

public class DateTools {
    //（1）定义一个isLeapYear方法，可以判断year是不是闰年
    public static boolean isLeapYear(int year){
/*        if(year%4==0 && year%100!=0 || year%400==0){
            return true;
        }else{
            return false;
        }*/

        return year%4==0 && year%100!=0 || year%400==0;
    }

    //（2）定义一个totalDaysOfYear方法，返回year年的总天数
    public static int totalDaysOfYear(int year){
        return isLeapYear(year)? 366 : 365;
    }

        /*
    public static void main(String[] args) {
        int year = 2023;
        System.out.println(year +"是闰年吗？" + isLeapYear(year));
        System.out.println(year  +"的总天数：" + totalDaysOfYear(year));
    }
    */
}
