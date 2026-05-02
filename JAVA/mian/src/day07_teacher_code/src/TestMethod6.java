package day07_teacher_code.src;

public class TestMethod6 {
    //功能：完成打印m行n列由某符号组成的矩形
    public static void printRectangle(int m, int n, char c){//有参无返回值
        for(int i=1; i<=m; i++){
            for(int j=1; j<=n; j++){
                System.out.print(c);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        printRectangle(5,10, '@');
        System.out.println("=================================");
        printRectangle(3,4, '6');
    }
}
