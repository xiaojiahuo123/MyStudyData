package day06_teacher_code.src;

public class TestArrayMax4 {
    public static void main(String[] args) {
        //元素是随机产生的,(-100,0]
        int[] arr = new int[10];//写完这句数组里面的元素是默认值，int类型的默认值是0

        //解决方案一：先产生所有的随机数
        for (int i = 0; i < arr.length; i++) {
            arr[i] = -(int) (Math.random() * 100);
            System.out.print(arr[i] + " ");
        }
        //到这里为止，元素值已经是确定的了

        int max = arr[0];//这一行代码 max =第1个元素的值
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > max){
                max = arr[i];
            }
        }
        System.out.println("max = " + max);
    }
}
