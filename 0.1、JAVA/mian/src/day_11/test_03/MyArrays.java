package day_11.test_03;

public class MyArrays {
    public static void sort(Object[] arr){
        for(int i=1; i<arr.length; i++){
            for(int j=0; j<arr.length-i; j++){
                //arr[j]和arr[j+1]
                //如果arr[j]要拥有compareTo方法，那么arr[j]对应的类型必须实现Comparable接口
                /*
                这里咱们约定好，如果要用sort方法排序，那么这数组中的元素的类，必须实现Comparable接口，
                重写compareTo方法，否则就算你调用这个sort，我也不能给你排序，
                会报ClassCastException错误。
                 */
                Comparable c = (Comparable) arr[j];//让arr[j]的类型以Comparable类型呈现
//                这里之所以这样可行，是因为Student类实现了Comparable接口，所以他作为对象调用这个类的这个方法的时候是可行的
                if(c.compareTo(arr[j+1]) > 0){
                    Object temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}
