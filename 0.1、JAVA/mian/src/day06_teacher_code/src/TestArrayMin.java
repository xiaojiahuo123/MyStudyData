package day06_teacher_code.src;

public class TestArrayMin {
    public static void main(String[] args) {
        int[] arr = {5, 6, 2, 7, 8, 1, 3};

        //故事：猴子掰最小的玉米
        //思路：
        //（1）先假设第1个元素是最小的
        int min = arr[0];

        //（2）用后面的元素与min比较，有比min小的，就替换min变量的值
        //这里i从1开始，表示元素的查找范围是[1, arr.length-1]，把[0]排除了
        for(int i=1; i<arr.length; i++){
            if(arr[i] < min){
                min = arr[i];
            }
        }
        System.out.println("min = " + min);
    }
}
