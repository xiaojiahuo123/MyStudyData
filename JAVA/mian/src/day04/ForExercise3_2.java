package day04;

public class ForExercise3_2 {
    public static void main(String[] args) {
        //3、从1循环到150并在每行打印一个值，另外在每个3的倍数行上打印出“foo”,
        // 在每个5的倍数行上打印“biz”,在每个7的倍数行上打印输出“baz”。

        /*for(int i=1; i<=150; i++){ //这里写i++或++i或i+=1或i=i+1都可以
            String str = "" + i;//""空字符串
            if(i%3==0){
                str += "\tfoo";
            }
            if(i%5==0){
                str += "\tbiz";
            }
            if(i%7==0){
                str += "\tbaz";
            }
            System.out.println(str);
        }*/

        for (int i = 1; i <= 150; i++) { //这里写i++或++i或i+=1或i=i+1都可以
            String str = "" + i;//""空字符串
            str += i % 3 == 0 ? "\tfoo" : "";
            str += i % 5 == 0 ? "\tbiz" : "";
            str += i % 7 == 0 ? "\tbaz" : "";
            System.out.println(str);
        }
    }
}
