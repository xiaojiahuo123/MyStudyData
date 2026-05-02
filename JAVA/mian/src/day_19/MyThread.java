package day_19;

public class MyThread extends Thread {
    @Override
    public void run() {
        //例如：打印1-10的偶数
        for(int i=2; i<=10; i+=2){
            System.out.println("偶数：" + i);
        }
    }

}
