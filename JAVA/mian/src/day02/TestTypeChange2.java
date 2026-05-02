package day02;

public class TestTypeChange2 {
    public static void main(String[] args) {
        byte b = 1;
        short s = 2;
        /*
        编译器，看到字面量1和2的时候，如果它们赋值给byte，short时，会判断它们在不在byte，short范围，
        如果在他们范围内，可以正常赋值。
         */
        char c = 'a';
        int i = 58;
        float f = 2.1f;
        System.out.println(b + s + c + i + f);//160.1
    }
}
