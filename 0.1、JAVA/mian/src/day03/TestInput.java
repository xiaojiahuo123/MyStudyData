package day03;

import java.util.Scanner; //导包，告诉编译器和JVM去哪里找到这个工具类，JRE中包含很多核心类库

public class TestInput {
    public static void main(String[] args) {
        /*
        这句代码创建了一个Scanner类的对象（这里忽略对象的概念）
        这句代码中只有input是可以变的，其余是固定的。
        input在这里就是一个变量名或对象名。它是标识符之一，可以由程序员自己取名字。
        这里取名为input，想要代表输入的意思

        System.in ：系统输入
        System.out：系统输出
         */

        Scanner input = new Scanner(System.in);

        System.out.print("请输入姓名：");

        /*
        调用Scanner工具类的方法来从键盘接收数据，把这个数据赋值给合适类型的变量
        调用，方法，都是新概念，先不管它
         */
        String name = input.next();

        System.out.print("请输入年龄：");
        int age = input.nextInt();

        System.out.print("请输入体重：");
        double weight = input.nextDouble();

        System.out.print("是否已婚（true/false）：");
        boolean marry = input.nextBoolean();

        System.out.print("请输入性别：");
//        char gender = input.nextChar();
        /*
        Scanner类在设计时考虑到使用String最多，所以输入String的方法，next()
        认为输入单个字符的情况很少，所以没有提供单独的nextChar()，
        如果你确实需要输入单个字符，那么可以从String中提取1个字符，
        charAt(index)，index=0,表示取第1个字符，这个index就是后面要学习的数组的下标概念
        charAt(index)，index=1,表示取第2个字符
        charAt(index)，index=2,表示取第3个字符
         */
        char gender = input.next().charAt(0);


        System.out.println("name = " + name);
        System.out.println("age = " + age);
        System.out.println("weight = " + weight);
        System.out.println("marry = " + marry);
        System.out.println("gender = " + gender);


        input.close();//释放资源，当前程序占用了键盘等系统资源，用完之后需要释放一下
    }
}
