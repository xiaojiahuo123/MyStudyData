package day02;

public class TestChar3 {
    public static void main(String[] args) {
        System.out.println('\'');
        System.out.println('"');

        System.out.println("\"");
        System.out.println("hello\tworld\tjava");
        System.out.println("haha\thi\tchai");

        System.out.println("hello\bworld\bjava");//hellworljava
        //\b相当于退一格
        System.out.println("hello\rworld\rjava");//java
        /*
        hello遇到\r回车结束本行，光标回到本行开头，重新输出world，遇到\r回车结束本行，光标回到本行开头，重新输出java，所以最后只看到java
         */
        System.out.println("hello\nworld\njava");//java
        /*
        hello
        world
        java
         */

    }
}
