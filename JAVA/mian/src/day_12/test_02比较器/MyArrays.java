package day_12.test_02比较器;

import java.util.Comparator;

public class MyArrays {
    public static void sort(Comparable[] arr){//接口的对象数组进行排序
        for(int i=1; i<arr.length; i++){
            for(int j=0; j<arr.length-i; j++){
                //arr[j] > arr[j+1] 会返回正整数
                if(arr[j].compareTo(arr[j+1]) > 0 ){
                    Comparable temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
 /*
多态机制的体现
这个排序机制充分体现了Java的多态性：
1.MyArrays.sort 方法接收的是 Comparable[] 类型的参数，但实际传入的是 Student[] 类型
2. 在方法内部调用 arr[j].compareTo(arr[j+1]) 时，会根据对象的实际类型（Student）调用对应的 compareTo 方法
3. 这种设计使得 sort 方法可以对任何实现了 Comparable 接口的对象数组进行排序，具有很高的通用性
这里的向上转型之所以能够成功，主要在于Student实现了Comparable接口（继承了）
 */
    public static void sort1(Comparator o,Object[] arr){
        for(int i=1; i<arr.length; i++){
            for(int j=0; j<arr.length-i; j++){
                //用sc对象compare方法，比较两个学生对象的大小
                if(o.compare(arr[j], arr[j+1]) > 0){
                    Object temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}
