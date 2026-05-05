package day_13.test_01异常;

import java.util.InputMismatchException;
import java.util.Scanner;

public class TestTryCatch {
    public static void main(String[] args) {
        //从控制台输入两个正整数，求它们的商。
        Scanner input = new Scanner(System.in);
        int a = 0;

        while (true) {
            try {
                //选中要用try-catch包围的代码，按快捷键Ctrl + Alt + T
                System.out.print("请输入第1个正整数：");
                a = input.nextInt();
                break;//如果input.nextInt()没有发生异常，那么break;会执行，catch不走。如果input.nextInt()发生异常了，break;不执行，跳到catch执行
            } catch (InputMismatchException e) {//当然你写它的笼统的父类Exception也可以。
                //打印异常
                //方式一：
                System.out.println(e);//普通信息的打印
                //方式二：
                // System.err.println(e);//错误信息的打印，默认用红色打印错误信息
                //方式三：
                // e.printStackTrace();//异常自带的标准的打印方式（前期一般用它）

                //把错误的不符合int类型的数据读取掉
                input.nextLine();//读取一整行，这里没有接收，因为这是错误的数据，不是我们要的数据
            }
        }

        int b;
        while(true) {
            try {
                System.out.print("请输入第2个正整数：");
                b = input.nextInt();
                if (b == 0) {
                    System.out.println("除数不能为0，请重新输入！");
                }else{
                    break;
                }
            } catch (Exception e) {
                //把错误的不符合int类型的数据读取掉
                input.nextLine();//读取一整行，这里没有接收，因为这是错误的数据，不是我们要的数据
            }
        }

        if(a<0){
            a = -a;//写法1，求负数的绝对值
        }
        b = Math.abs(b);//写法2，求绝对值

        int result = a / b;
        System.out.println("result = " + result);

        input.close();

    }
}
