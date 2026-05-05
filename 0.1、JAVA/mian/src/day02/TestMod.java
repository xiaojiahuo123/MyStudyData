package day02;

public class TestMod {
    public static void main(String[] args) {
        System.out.println(8 % 3);//商是2，余数是2
        System.out.println(3 % 8);//商是0，余数是3

        System.out.println(8 % -3);//商是-2，余数是2
        //被除数 ÷ 除数 = 商 ... 余数
        //被除数 = 除数 x 商 + 余数
        System.out.println(-8 % 3);//商是-2，余数是-2
        System.out.println(-8 % -3);//商是2，余数是-2

        System.out.println("====================");
        int num = 516;//3位数 000 - 999
        System.out.println("个位：" + num % 10);
        System.out.println("十位：" + num / 10 % 10);
        System.out.println("百位：" + num / 100);
    }
}
