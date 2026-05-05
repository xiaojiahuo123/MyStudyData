package day06_teacher_code.src;

public class TestArrayMax2 {
    public static void main(String[] args) {
        //元素是随机产生的,[0,100)
        int[] arr = new int[10];//写完这句数组里面的元素是默认值，int类型的默认值是0

        int max = arr[0];//这一行代码 max = 0
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int)(Math.random()*100);
            if(arr[i] > max){
                max = arr[i];
            }
            System.out.print(arr[i] + " ");
        }
        System.out.println("max = " + max);
    }
}
