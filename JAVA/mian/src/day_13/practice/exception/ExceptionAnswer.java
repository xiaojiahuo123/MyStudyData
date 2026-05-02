package day_13.practice.exception;

// Q3 编程题答案：自定义异常类
class AgeIllegalException extends Exception {
    public AgeIllegalException(String msg) { super(msg); }
}

public class ExceptionAnswer {
    public static void checkAge(int age) throws AgeIllegalException {
        if (age < 0 || age > 150) throw new AgeIllegalException("年龄非法");
    }
    // Q4 理解题答案：finally块用于保证无论是否发生异常，都会执行收尾操作，如资源释放。
}
