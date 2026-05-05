package day07_teacher_code.src;

public class TestParam {
    public static void main(String[] args) {
        System.out.println(add(1,2));//(1,2)是实参
        //System.out.println(add(1.2,2));//(1.2,2)是实参，1.2实参的类型是double>形参a的类型int
        //System.out.println(add(1,2,3));//实参的个数与形参不匹配

        test("hello",1);
        //test(1,"hello");//实参的顺序与形参的顺序不一致
    }

    public static int add(int a, int b){//(int a,int b)是形参
        return a + b;
    }

    public static void test(String s, int a){
        System.out.println("s = " + s);
        System.out.println("a = " + a);

    }
}
