package day07_teacher_code.src;

public class TestMethod7 {
    //功能：随机产生1个[0,100)的整数
    public static int getANumberFrom0To100(){//无参有返回值
        return (int)(Math.random()*100);
    }

    public static void main(String[] args) {
        //有返回值的方法调用写完之后，可以 是 方法名().var 来自动生成左边的变量，或者 方法();按Ctrl + Alt + V
        int result = getANumberFrom0To100();
        System.out.println("result = " + result);
    }
}
