package day05_teacher_code.src;

import java.util.Scanner;

public class MyLianxi_02 {
    public static void main(String[] args) {
        String[] Month = {"January","February","March","April","May","June","July","August","September","October","November","December"};
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入月份 ： " );
        int month = scanner.nextInt();
        if (month >= 1 && month <=12){
            System.out.println("对应的英文是：" + Month[month-1]);
        }else {
            System.out.println("输入错误！");
        }
        scanner.close();
/*        在 Java 中使用Scanner后调用scanner.close()主要有以下几个原因：
        释放资源：Scanner通常会关联一个输入流（如System.in、文件流等），这些流属于系统资源，有限且宝贵。
        如果不关闭Scanner，可能导致底层输入流无法被正确释放，造成资源泄漏。
        避免资源冲突：对于像System.in这样的标准输入流，如果通过Scanner关闭后，其他地方再想使用System.in会抛出异常，
        因为流已经被关闭。但这恰恰体现了关闭的重要性 - 明确资源的生命周期，避免不同代码段对同一资源的争夺。
        符合 Java 资源管理规范：所有实现了AutoCloseable接口的类（Scanner就是其中之一）都应该在使用完毕后关闭，
        这是 Java 资源管理的最佳实践。从 Java 7 开始，还可以使用 try-with-resources 语法自动关闭这些资源：*/
    }
}
