package day07_teacher_code.src;

public class TestMethod5 {
    //功能：完成打印5行5列由*组成的矩形
    public static void print5Line5ColumnRectangle(){//无参无返回值
        for(int i=1; i<=5; i++){
            for(int j=1; j<=5; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
//        System.out.println(print5Line5ColumnRectangle());//错误，因为print5Line5ColumnRectangle方法没有结果返回，不能打印结果
        print5Line5ColumnRectangle();
    }
}
