package day_13.test_01异常.test_01_01;

import org.junit.Test;

import java.util.Scanner;

/*
* 题目要求
定义一个 自定义异常类 AgeIllegalException，继承 Exception，用于表示 “年龄不合法”（如年龄 <0 或 >150）。
编写一个方法 checkAge(int age)，如果年龄不合法，抛出 AgeIllegalException，并传入提示信息（如 “年龄不能小于 0！”）。
在 main 方法中调用 checkAge()，传入不同的年龄值（如 20、-5、200），使用 try-catch 捕获 AgeIllegalException，并打印异常信息。
* */
public class test_004 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("请输入年龄:");
            int age = sc.nextInt();
            checkAge(age);
        } catch (AgeIllegalException e) {
            //throw new RuntimeException(e);
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }

    public static void checkAge(int age) throws AgeIllegalException {
        /*
 - AgeIllegalException 继承自 Exception 类（非 RuntimeException ），属于 检查型异常
- Java语言规定： 所有检查型异常必须在方法签名中使用 throws 声明，或者在方法体内使用 try-catch 捕获,也就是捕获后不会编译报错
- 如果不加第12行的 throws AgeIllegalException 声明，直接在第14行抛出该异常，违反了Java的编译规则
- 如果方法中抛出了检查型异常但未声明，编译器会报错并拒绝编译通过
- 这种机制确保开发者必须显式处理潜在的异常情况，提高程序的健壮性
        * */
        if (age <= 0) {
            throw new AgeIllegalException();
        }
    }
}
