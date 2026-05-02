package day_13.test_01异常;

import java.util.InputMismatchException;
import java.util.Scanner;

/*
* 练习题 2：数组越界异常（ArrayIndexOutOfBoundsException）
题目要求
定义一个长度为 5 的整数数组 int[] arr = {1,2,3,4,5}，从控制台接收一个整数 index，输出数组中对应索引的元素。
如果输入的索引超出数组范围（<0 或 ≥5），捕获 ArrayIndexOutOfBoundsException，提示 “索引越界！数组长度为 5，请输入 0-4 之间的索引”。
如果输入的不是整数，捕获 InputMismatchException，提示 “请输入合法的整数索引！”。
异常处理后，程序正常结束（不崩溃）。
* */
public class test_001 {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("请输入整数索引");
            int index = sc.nextInt();
            System.out.println("第"+ index + "元素的值为:" + arr[index]);
        } catch (ArrayIndexOutOfBoundsException e) {
            //throw new RuntimeException(e);
            System.out.println(e.getMessage());
            System.out.println("索引越界！数组长度为 5，请输入 0-4 之间的索引");
        }catch (InputMismatchException e){
            System.out.println("请输入合法的整数索引！");
        } finally {
            sc.close();
        }

    }
}
