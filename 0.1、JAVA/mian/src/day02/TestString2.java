package day02;

public class TestString2 {
    public static void main(String[] args) {
        int num = 15;
        String str = num + "";//""是一个空字符串，没有任何字符
        System.out.println(str);

        String str2 = "15";
//        int num2 = (int)str2;
        //强制转换不可以
        int num2 = Integer.parseInt(str2); //后面要学习的方法
    }
}
