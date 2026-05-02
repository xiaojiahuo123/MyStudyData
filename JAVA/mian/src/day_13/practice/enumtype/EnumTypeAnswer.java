package day_13.practice.enumtype;

public class EnumTypeAnswer {
    enum Season { SPRING, SUMMER, AUTUMN, WINTER }
    public static void main(String[] args) {
        Season s = Season.SUMMER;
        System.out.println(s);
    }
    // Q14 理解题答案：枚举类让常量更安全、可读性更高，避免魔法值。
}
