package day_19;

public class TestMyThread {
    public static void main(String[] args) {
        MyThread m = new MyThread();
        m.start();


        //打印1-10的奇数
        for(int i=1; i<=10; i+=2){
            System.out.println("奇数：" + i);
        }
    }
}
