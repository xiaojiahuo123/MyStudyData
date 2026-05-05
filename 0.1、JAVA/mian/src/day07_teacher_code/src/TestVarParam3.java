package day07_teacher_code.src;

public class TestVarParam3 {
    public static void main(String[] args) {
        System.out.println(concat("[","]","-","hello","world","java","atguigu"));
        System.out.println(concat("","","-","hello","world","java","atguigu"));
        System.out.println(concat("","",",","hello","world","java","atguigu"));
        System.out.println(concat("[","]",","));
    }

    //实现拼接n个字符串，拼接的时候可以指定开头的符号，结尾的符号，中间连接的符号
    //hello  world  java   atguigu
    //[hello,world,java,atguigu]
    //hello-world-java-atguigu
    public static String concat(String start, String end, String middle, String... args){
        String str = start;

        for (int i = 0; i < args.length; i++) {
            if(i==0){
                str += args[i];
            }else{
                str += middle + args[i];
            }
        }

        str += end;
        return str;
    }
}
