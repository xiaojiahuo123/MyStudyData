package day02;

public class Exercise8 {
    public static void main(String[] args) {
        /*boolean flag = false;
        System.out.println(flag == true ? "成立" : "不成立");*/
        /*
        ==是比较运算符，取flag变量的值来与true比较， false == true 不成立
         */

        /*boolean flag = false;
        System.out.println((flag = true) ? "成立" : "不成立");*/
        /*
        等价于
        （1）先把flag的值修改为true，因为=是赋值运算符，不是比较运算符
        （2）再取flag变量的值当做条件使用，true ? "成立" : "不成立"  成立
         */
        /*flag = true;
        System.out.println(flag? "成立" : "不成立");*/


        /*boolean flag = false;
        System.out.println(flag ? "成立" : "不成立");*/
        //直接取flag变量的值当做条件使用，false ? "成立" : "不成立"    结果不成立


   /*     boolean flag = false;
        System.out.println(!flag ? "成立" : "不成立");*/
        /*
        (1)先取flag的值 false
        (2)!false 当条件， !false是true  成立
         */

        int a = 1;
        System.out.println(a == 1 ? "成立" : "不成立");
//        System.out.println(a = 1 ? "成立" : "不成立");//错误 ，1当条件是不可以的，Java中只有true和false可以当条件
    }
}
