package day_08.com.atguigu.Test1;

public class MyDate {
    public int MYyear;
    public int MYmonth;
    public int MYday;
    public static final int[] COMMON_YEAR_MONTHS = {31,28,31,30,31,30,31,31,30,31,30,31};
    public static final String[] MONTH_NAME = {"January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"};
//    `public boolean isLeapYear()`：用于判断year年是不是闰年
    public boolean isLeapYear(){
        // 闰年规则：能被4整除且不能被100整除，或者能被400整除
        return (MYyear % 4 == 0 && MYyear % 100 != 0) || (MYyear % 400 == 0);
    }
//    `public int totalDaysOfYear()`：用于返回year年的总天数
    public int totalDaysOfYear(){
    // 平年365天，闰年366天
    return isLeapYear() ? 366 : 365;

    // 另一种实现方式：通过累加每个月的天数
        /*
        int totalDays = 0;
        for (int i = 0; i < 12; i++) {
            // 2月份在闰年需要加1天
            if (i == 1 && isLeapYear()) {
                totalDays += 29;
            } else {
                totalDays += COMMON_YEAR_MONTHS[i];
            }
        }
        return totalDays;
        */
   }
//`public int daysOfMonth()`：用于返回month月的总天数
    public int daysOfMonth(){
      int days = COMMON_YEAR_MONTHS[MYmonth-1];
      if(MYmonth == 2 && isLeapYear()){
        days ++;
      }
      return days;
    }
//`public int daysOfYear()`：用于返回year年month月day日是这一年的第几天
public int daysOfYear(){
    // 校验月份合法性（避免数组越界）
    if (MYmonth < 1 || MYmonth > 12 || MYday < 1 || MYday > daysOfMonth()) {
        throw new IllegalArgumentException("无效的日期：" + MYyear + "-" + MYmonth + "-" + MYday);
    }

    int days = 0;
    // 累加当前月份之前所有月份的天数（1月到MYmonth-1月）
    for (int i = 1; i < MYmonth; i++) {
        // 月份i对应的数组索引是i-1
        if (i == 2 && isLeapYear()) {
            days += 29; // 闰年2月29天
        } else {
            days += COMMON_YEAR_MONTHS[i - 1]; // 平年或其他月份
        }
    }

    // 加上当月的天数
    days += MYday;

    System.out.println("这是" + MYyear + "年的第" + days + "天");
    return days;
}
//`public String monthName`：用于返回month月的名称
public String monthName(){
        return MONTH_NAME[MYmonth-1];
}
//`public String getInfo()`：用于返回“year年month月day日”字符串信息
    public String getInfo(){
        return MYyear +"年" + MYmonth + "月" + MYday +"日";
    }
}
