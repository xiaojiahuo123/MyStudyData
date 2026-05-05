package day06_teacher_code.src;

public class TestArrayMax3 {
    public static void main(String[] args) {
        //元素是随机产生的,(-100,0]
        int[] arr = new int[10];//写完这句数组里面的元素是默认值，int类型的默认值是0

        int max = arr[0];//这一行代码 max = 0
        for (int i = 0; i < arr.length; i++) {
            arr[i] = -(int)(Math.random()*100);
            if(arr[i] > max){//这句代码永远不成立
                max = arr[i];
            }
            System.out.print(arr[i] + " ");
        }
        System.out.println("max = " + max);//结果错误
    }
}
