package day_13.test_01异常;

import java.io.FileNotFoundException;
import java.io.FileReader;

/*
* 题目要求
编写一个程序，尝试读取本地磁盘上的一个不存在的文件（如 D:/test.txt）。
使用 FileReader 类（需要导入 java.io.FileReader 和 java.io.FileNotFoundException）。
捕获 FileNotFoundException，并通过异常对象的 getMessage() 方法打印 “文件未找到的详细信息”。
思考：FileReader 的构造方法是 “checked 异常” 还是 “ unchecked 异常”？为什么必须用 try-catch 处理（或 throws 声明）？
*
* FileNotFoundException 继承自 IOException，而 IOException 是 checked 异常，因此必须在编译时处理。
* checked 异常的设计哲学是：强制程序员处理可能发生的、可预期的错误情况
*
* */
public class test_003 {
    public static void main(String[] args) {
        try {
            FileReader fr = new FileReader("D:/test.txt");
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }
}
