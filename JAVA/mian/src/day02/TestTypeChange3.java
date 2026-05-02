package day02;

public class TestTypeChange3 {
    public static void main(String[] args) {
        byte b1 = 1;
        byte b2 = 2;
       // byte b3 = b1 + b2;
        /*
        b1 + b2 升级为int，此时b1和b2是变量，每一个变量的范围是-128~127，计算可能超过byte范围，
        这里直接报错，不会检查值 在不在byte范围。

        byte相加用的是int类型指令，所以结果是int
         */
        int b3 = b1 +b2;
        System.out.println("b3 = " + b3);

        char c1 = 'a';
        char c2 = '0';
//        char c3 = c1 + c2;//c1+c2是int，int>char，无法赋值
        System.out.println(c1 + c2);//c1+c2虽然升级为int，但是println支持int结果
        // 97 + 48 = 145
    }
}
