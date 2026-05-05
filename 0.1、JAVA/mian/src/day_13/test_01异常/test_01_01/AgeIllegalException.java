package day_13.test_01异常.test_01_01;

public class AgeIllegalException extends Exception{
    public AgeIllegalException() {
        System.out.println("年龄不合法!");
    }

    public AgeIllegalException(String message) {
        super(message);
    }

    public AgeIllegalException(String message, Throwable cause) {
        super(message, cause);
    }

    public AgeIllegalException(Throwable cause) {
        super(cause);
    }

    public AgeIllegalException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
