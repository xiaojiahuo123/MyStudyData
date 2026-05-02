package day02;

public class PluginDemo {
    public static void main(String[] args) {
        int a = 3;
        int b = 2;
        int c = 1;

        int max = a > b ? a : b;
        max = max > c ? max : c;
        System.out.println("max = " + max);
    }
}
