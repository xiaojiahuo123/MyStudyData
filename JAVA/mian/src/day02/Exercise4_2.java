package day02;

public class Exercise4_2 {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;

        //方案二：了解
        //有缺陷，对数据类型，和数据值的范围有要求
        a = a + b; //新的a = 旧的a + 旧的b
        b = a - b;//新的b = 新的a - 旧的b = 旧的a + 旧的b - 旧的b = 旧的a
        a = a - b;//更新的a = 新的a - 新的b = 旧的a + 旧的b - 旧的a = 旧的b
        System.out.println("a = " + a);//a=2
        System.out.println("b = " + b);//b=1
    }
}
