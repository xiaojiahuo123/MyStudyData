package day06_teacher_code.src;

public class MyLianxi_02 {
    public static void main(String[] args) {
        int[] arr = {5, 6, 8, 7, 8, 9, 3, 9};

        /*
        方案二：
        (1)假设max表示最大值，初始化为arr[0]
        (2)假设maxIndexStr表示最大值的下标，它是String，初始化为"0"

         */
        int max = arr[0];
        String maxIndexStr = "0";
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > max){
                max = arr[i];
                maxIndexStr = i + "";
            }else if(arr[i] == max){
                maxIndexStr += "," + i;
            }
        }
        System.out.println("max = " + max);
        System.out.println("maxIndexStr = [" + maxIndexStr+"]");
    }
}
