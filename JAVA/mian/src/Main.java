public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        //把光标定位到()里面，按Ctrl + P
        //输出一个整数18
        System.out.println(18);//18默认是int类型
        System.out.println(18L);//18L明确是long类型
        //输出一个小数1.8
        System.out.println(1.8);//1.8默认是double类型
        System.out.println(1.8F);//1.8F明确是float，这里F大小写都可以

        //输出单个字符
        System.out.println('男'); //单引号
//        System.out.println('hi'); //错误，hi有2个字符，单引号里面只能有1个字符
        //  System.out.println('');//单引号里面有且只有1个字符

        //输出布尔值
        System.out.println(true);
        System.out.println(false);

        System.out.println("atguigu");//双引号，这个是字符串
        System.out.println("");//双引号里面可以空着，称为空字符串

        System.out.println("======================");
        System.out.println('a' + 'b');//可以算术运算符 + ,-,*,/等
        //'a'对应的编码值是97，'b'是98
        System.out.println("a" + "b");//拼接
        /*
        + 只要没有字符串参与就是求和

        + 只有有字符串参与就是拼接
         */
        int age = 18;
//        String Hua = '他的年龄是';
        System.out.println("他的年龄是"+age);
    }
}