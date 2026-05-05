package day04;

public class TestDoWhile {
    public static void main(String[] args) {
        //输出5次我爱尚硅谷
        int i= 1;
        do{
            System.out.println("我爱尚硅谷" + i);
            i++;
        }while(i<=5);
        System.out.println("i = " + i);
    }
}
