package day_13.test_01异常;

import java.io.FileReader;

/*
* 练习题 3：多异常的顺序匹配（catch 块顺序）
题目要求
思考并编写代码验证：catch 块的顺序为什么必须是 “子类异常在前，父类异常在后”？
定义一个方法 testException()，在方法中故意抛出 NullPointerException（子类异常）。
尝试两种 catch 顺序：
先 catch NullPointerException，再 catch Exception（父类异常）—— 观察是否能正常捕获子类异常。
先 catch Exception，再 catch NullPointerException—— 观察编译器是否报错，或运行时是否能捕获子类异常。
结合结果，说明为什么 catch 块必须按 “子类→父类” 顺序排列
*
*
* 顺序 1（子类→父类）：正常捕获 NullPointerException，因为异常会匹配第一个符合的 catch 块。
顺序 2（父类→子类）：编译器报错 “Unreachable catch block for NullPointerException”，
* 因为 Exception 是所有异常的父类，会先捕获所有异常，子类异常的 catch 块永远执行不到。
结论：catch 块必须按 “子类异常在前，父类异常在后” 排列，否则子类异常的 catch 块会被父类异常 “屏蔽”，无法执行。
* */
public class test_002 {
    public static void main(String[] args) {
        try {
            FileReader fr = new FileReader("D:/test.txt");
        } catch (Exception e) {
// 打印异常详细信息
            System.out.println("文件未找到：" + e.getMessage());
        }


    }
}
