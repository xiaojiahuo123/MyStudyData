package day02;

public class Exercise4 {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;

        /*
        方案一：必须掌握的方案，适用于所有数据类型，包括后面的引用数据类型
         */
        int temp = a;//把a变量的值 倒入 temp这个杯子
        a = b; //把b变量的值 倒入 a这个杯子
        b = temp; //把temp变量的值 倒入 b这个杯子
        System.out.println("temp = " + temp);//temp=1
        System.out.println("a = " + a);//a=2
        System.out.println("b = " + b);//b=1
    }
}
