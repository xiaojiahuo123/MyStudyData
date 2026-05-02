package day07_teacher_code.src;

public class CompareTools {
    /*
    定义3个方法，分别可以比较两个整数、两个小数、两个字符的大小。以a,b为例
    结果都要求 a > b 返回正整数
    结果都要求 a < b 返回负整数
    结果都要求 a == b 返回0

    注意：方法的返回值类型与方法的形参类型没有必然联系，
         方法的返回值类型由“结果”来决定
         上面分析了结果是正整数、负整数、0，所以是int类型
     */

/*    public static int compare(int a,int b){
        if(a>b){
            return 1;
        }else if(a<b){
            return - 1;
        }else{
            return 0;
        }
    }*/
/*    public static int compare(int a,int b){
        if(a>b){
            return 1;//return可以返回结果，同时结束当前方法的执行
        }else if(a<b){
            return - 1;
        }

        return 0;
    }*/
    public static int compare(int a,int b){
        return a-b;
    }
    /*
    4.3 与 4.6 比较
     */
/*    public static int compare(double a,double b){
        return (int) (a-b);//不够完美
    }*/
    public static int compare(double a,double b){
        if(a>b){
            return 1;
        }else if(a<b){
            return - 1;
        }else{
            return 0;
        }
    }
    public static int compare(char a,char b){
        return a-b;//这里自动用char字符的编码值计算
    }

}
