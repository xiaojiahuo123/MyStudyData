package day04;

import java.util.Random;
import java.util.Scanner;

public class MyLianxi_01 {
    public static void main(String[] args) {
        System.out.println("-------------------欢迎进入游戏------------------");
        Random rand = new Random();
        int rand1 = rand.nextInt(1,7);
//        若要生成 [min, max) 范围内的整数（左闭右开，即包含min，不包含max），通用公式为：
//        (int) (Math.random() * (max - min) + min)
//        若要生成 [min, max] 闭区间（包含max），公式应为
//        (int) (Math.random() * (max - min + 1) + min)  其实可以直接写清楚一些，比如：(int) (Math.random() * max + min)
        int rand2 = rand.nextInt(1,7);
        int rand3 = rand.nextInt(1,7);
        //nextInt(int origin, int bound)是 Java 17 引入的新方法，在更早的版本（如 Java 8）中无法使用，会导致编译错误
        System.out.println("-----------请输入你认为的结果，两次机会------------");
        Scanner scanner = new Scanner(System.in);
        String Scan1 = scanner.next();
        String Scan2 = scanner.next();
//        String Scan3 = scanner.next();
        String str1 = "";
        if (rand1 == rand2 && rand1== rand3){
            str1 = "豹子";
        } else if ((rand1 + rand2 + rand3) >= 9) {
            str1 = "大";
        }else {
            str1 = "小";
        }
        //对于字符串来说，不能用==字符串的内容，因为字符串不是基本数据类型
        System.out.println(str1.equals(Scan1) ? "恭喜你猜对了":"很遗憾猜错了");
        System.out.println(str1.equals(Scan2) ? "恭喜你猜对了":"很遗憾猜错了");
        System.out.println("三个数分别是："+rand1+","+rand2+","+rand3);
    }
}
