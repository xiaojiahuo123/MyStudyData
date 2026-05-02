package day05_teacher_code.src;

public class TestArrayArithmeticDemo2 {
    public static void main(String[] args) {
        /*
        需求：随机产生10个[0,100)的整数，打印显示它们
        统计它们中偶数的个数，3的倍数的个数
         */
        //(1)声明一个int[]类型的数组，长度为10
        int[] arr = new int[10];

        //(2)随机产生10个[0,100)的整数，放到数组中，打印显示它们
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int)(Math.random()*100);
            System.out.print(arr[i]+" ");
        }
        System.out.println();

        int two = 0;
        int three = 0;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] % 2 == 0){
                two++;
                System.out.println(arr[i] +"是偶数");
            }
            if(arr[i] % 3 == 0){
                three++;
                System.out.println(arr[i] +"是3的倍数");
            }
        }
        System.out.println("偶数："  + two);
        System.out.println("3的倍数："  + three);
    }
}
