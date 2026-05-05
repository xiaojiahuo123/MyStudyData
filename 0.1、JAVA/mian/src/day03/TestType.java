package day03;

public class TestType {
    public static void main(String[] args) {
        //Java编译器对于字面量值的判断
        //如果没有和参考的依据的话，整数字面量值默认是int类型
        //如果有可参考的依据的话，看情况
        byte b1 = 1;//此时右边的1可以看成是byte类型，因为可以参考b1前面的byte
        //byte b2 = 200;//200本来参考b2前面的byte，想要看成byte类型，但是byte的范围是-128-127，超过byte范围，只能看int算
        char c1 = 97;//此时97参考c1前面的char，看成char类型，对应的字符是'a'
//        char c2 = 70000;//70000参考c2前面的char，看成char类型，但是char编码值的范围是0-65535，超过范围

        System.out.println(true ? 'a' : 10);//10可以看成与'a'是同类型的char
        System.out.println(true ? 'a' : 70000);//70000超过char的范围的，所以只能看成int  'a'就必须转为97
    }
}
