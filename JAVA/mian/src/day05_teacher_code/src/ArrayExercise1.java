package day05_teacher_code.src;

public class ArrayExercise1 {
    public static void main(String[] args) {
        //随机产生5个[0,100)的偶数放到数组中 ，并遍历输出
        //(1)先声明数组，类型是int[]，长度是5
        int[] arr = new int[5];
        //所谓的“动态”初始化是指元素的具体值，需要在程序“运行时”，通过计算、键盘输入等方式确定的

        //(2)随机产生5个[0,100)的偶数放到数组中
        /*Random random = new Random();
        for (int i = 0; i < arr.length; i++) {
            arr[i] = random.nextInt(0,50) * 2;
        }*/
        /*
        Math.random() * 50：[0,50)的小数   46.6
        Math.random() * 50 * 2 :   93.2
        (int)(Math.random() * 50 * 2) :   93

        Math.random() * 50：[0,50)的小数   46.6
        （int)(Math.random() * 50) ： 46
        （int)(Math.random() * 50) * 2 :92
         */
        /*for (int i = 0; i < arr.length; i++) {
            arr[i] = (int)(Math.random() * 50) * 2;
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }*/

        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int)(Math.random() * 50) * 2;
            System.out.print(arr[i] + " ");
        }
    }
}
