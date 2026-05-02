package day_15.泛型.泛型方法;
/*【修饰符】 class 类名{
【修饰符】 <泛型字母> 返回值类型 方法名(【形参列表】){//在方法的返回值类型前面定义了新的<泛型字母>，这样的方法称为泛型方法

}
}*/
public class Example {
    public <T> void test1(T t){
        System.out.println(t + "test1");
    }

    public <T> void test2(T t){
        System.out.println(t + "test2");
    }
}
