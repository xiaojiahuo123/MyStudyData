package algorithm;

public class BasicArray {
    /*
     *数组元素之和
     */
    public static int sum(int[] arr){
        int sum = 0;
        for(int i = 0; i<arr.length; i++){
            arr[i] += arr[i];
            sum = arr[i];
        }
        return sum;
    }
    /*
     * 数组中最大值
     * */
    public static int max(int[] arr){
        int max = arr[0];
        for (int j : arr) {
            max = max > j ? max : j;
        }
        return max;
    }
    /*
     * 数组中最小值
     * */
    public static int min(int[] arr){
        int min = arr[0];
        for (int j : arr) {
            min = Math.min(min, j);
        }
        return min;
    }
    /*
     *查找value在arr数组中第一次出现的下标，如果不存在返回-1
     * */
    public static int indexOf(int[] arr, int value){
        int indexOf = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == value) {
                indexOf = i;
            }
        }
        return indexOf;
    }
    /*
     *查找value在arr数组中最后一次出现的下标，如果不存在返回-1
     * */
    public static int lastIndexOf(int[] arr, int value){
        // 数组为空时直接返回-1
        if (arr == null || arr.length == 0) {
            return -1;
        }
        int indexOf = -1;
        // 从数组末尾开始向前遍历
        for (int i = arr.length - 1; i >= 0; i--) {
            // 找到第一个匹配的值就返回其下标
            if (arr[i] == value) {
                indexOf =  i;
            }
        }
        return indexOf;
    }
    //    查找value在arr数组中出现的次数，如果不存在返回0
    public static int valueCount(int[] arr, int value){
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int count = 0;
        for(int i : arr){
            if(i == value){
                count++;
            }
        }
        return count;
    }
    //    实现元素从小到大排序
    public static void sort(int[] arr){
        if (arr == null || arr.length == 0) {
            System.out.println("数组不能为null!");
        }
        for (int i = 1; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length -1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    //    反转[start,end]范围内的元素
    public static void reverse(int[] arr, int start, int end){
        if (arr == null || arr.length == 0) {
            System.out.println("空数组或单元素数组无需处理");
        }
        if (start < 0 || end >= arr.length || start >= end) {
            return;  // 范围不合法无需处理
        }
        // 交换两端元素，向中间移动
        while (start < end) {
            // 交换元素
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            // 移动指针
            start++;
            end--;
        }
    }
    //    复制数组
    public static int[] copyOf(int[] arr, int newLength){
        // 处理原数组为null的情况
        if (arr == null) {
            return null;
        }

        // 处理新长度为负数的情况（按Java规范通常抛异常，这里简化处理返回空数组）
        if (newLength < 0) {
            throw new NegativeArraySizeException("新长度不能为负数");
        }
        int[] newArr = new int[newLength];
        // 确定需要复制的元素数量：不超过原数组长度，也不超过新数组长度
        int copyCount = Math.min(arr.length, newLength);
/*        for (int i = 0; i < arr.length; i++) {
            if (i > newLength -1){
                return newArr;
            }
            newArr[i] = arr[i];
        }*/
        for (int i = 0; i < copyCount; i++) {
            newArr[i] = arr[i];
        }
        return newArr;
    }
    //    String toString(int[] arr)：将元素拼接为"[元素1，元素2，......]"的字符串返回
    public static String MytoString(int[] arr){
        // 处理数组为null的情况
        if (arr == null) {
            return "[]";
        }
        // 处理空数组的情况
        if (arr.length == 0) {
            return "[]";
        }
        String str = "";
        for (int i = 0; i < arr.length; i++) {
            str = str + arr[i]+ ",";
        }
        str = "[" + str + "]";
        return str;
    }
}
