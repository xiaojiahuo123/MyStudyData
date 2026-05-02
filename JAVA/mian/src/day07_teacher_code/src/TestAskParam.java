package day07_teacher_code.src;

import java.util.Scanner;

public class TestAskParam {
    public static void main(String[] args) {
        int result = add();
        System.out.println("result = " + result);
        int sumResult1 = sum(5, 1);
        int x = (int)(Math.random()*100);
        int y = (int)(Math.random()*100);
        int sumResult2 = sum(x,y);
    }

    public static int add(){
        Scanner input = new Scanner(System.in);
        System.out.print("请输入a的值：");
        int a = input.nextInt();
        System.out.print("请输入b的值：");
        int b = input.nextInt();
        input.close();
        return a + b;
    }

    public static int sum(int a, int b){
        return a + b;
    }
}
