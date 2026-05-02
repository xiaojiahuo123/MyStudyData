package day_08.com.atguigu.test2;

//成员变量，俗称属性
public class MyDate {//自定义的日期类型
    public int year;
    public int month;
    public int day;

    /*public void setDate(int y, int m ,int d){
        year = y;
        month = m;
        day = d;
    }*/
    public void setDate(int year, int month ,int day){
        this.year = year;
        this.month = month;
        this.day = day;
        //左边代表的是当前对象的成员变量，右边是形参变量
        //this是当前对象，它是一个代词，要根据上下文才能推断它代表哪个对象
    }

    public String getDateInfo(){
//        return this.year+"-" + this.month+"-" + this.day;
        return year+"-" + month+"-" + day;
        //当成员变量与局部变量（形参也是局部变量）重名时，需要在成员变量前面加this.
        //如果没有重名问题，可以省略this.，直接访问本类的成员变量
    }
}
