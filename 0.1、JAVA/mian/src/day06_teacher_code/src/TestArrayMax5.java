package day06_teacher_code.src;

public class TestArrayMax5 {
    public static void main(String[] args) {
        //元素是随机产生的,
        int[] arr = new int[10];//写完这句数组里面的元素是默认值，int类型的默认值是0

        //解决方案二：产生随机数的同时，就找最大值
        int max = 0;//随便初始化一个
        for (int i = 0; i < arr.length; i++) {
//            arr[i] = -(int) (Math.random() * 100);
            arr[i] = (int) (Math.random() * 100);
            System.out.print(arr[i] + " ");
            if(i==0){//第1个元素的时候
                max = arr[0];//把max修改为第1个元素
            }else if(arr[i] > max){//不是第一个元素，让它与max比大小
                max = arr[i];
            }
        }

        System.out.println("max = " + max);
    }
}
