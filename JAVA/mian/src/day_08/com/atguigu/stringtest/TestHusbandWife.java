package day_08.com.atguigu.stringtest;

public class TestHusbandWife {
    public static void main(String[] args) {
        Husband h = new Husband();
        h.name = "张三";

        Wife w = new Wife();
        w.name = "翠花";

        h.wife = w;//给h.wife变量赋值一个Wife类型的对象
        w.husband = h;

        System.out.println("丈夫的姓名：" + h.name +"，他妻子的姓名：" + h.wife.name);
        System.out.println("妻子的姓名：" + w.name +"，她的丈夫的姓名：" + w.husband.name);
    }
}
