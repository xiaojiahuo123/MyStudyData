package day_14.Arrays;

import org.junit.Test;

import java.text.Collator;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Locale;

public class TestArrays {
    @Test
    public void test1() {
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println(Arrays.toString(arr));
        /*Arrays.toString(long[] a)实现的源码:
        *  public static String toString(long[] a) {
        if (a == null)
            return "null";
        int iMax = a.length - 1;
        if (iMax == -1)
            return "[]";

        StringBuilder b = new StringBuilder();
        b.append('[');
        for (int i = 0; ; i++) {
            b.append(a[i]);
            if (i == iMax)
                return b.append(']').toString();
            b.append(", ");
        }
    }
        * 
        - 数组元素拼接过程 ：

- 代码通过 for 循环遍历数组中的每个元素
- 在每次循环中，将当前元素 a[i] 追加到 StringBuilder 对象 b 的后面
- 对于非最后一个元素，还会添加逗号和空格(", ")作为分隔符
- 2.
循环结束条件与返回值处理 ：

- 当 i 等于 iMax (即 a.length - 1 ，最后一个元素的索引)时
- 代码执行 b.append(']') ，在字符串末尾添加结束括号
- 然后立即调用 toString() 方法将 StringBuilder 对象转换为普通 String 对象并返回
- 这种写法利用了 return 语句同时完成了添加结束符、转换字符串和返回结果三个操作
        */
        //[1, 2, 3, 4, 5]
    }

    @Test
    public void test2() {
        int[] arr = {11, 20, 13, 4, 15};
        System.out.println("排序前：" + Arrays.toString(arr));
        Arrays.sort(arr);
/*
首先调用 rangeCheck 方法验证索引范围是否合法（fromIndex >= 0，toIndex <= 数组长度，且fromIndex <= toIndex）
这是一种防御性编程，避免数组越界异常

调用实际排序算法
 核心排序逻辑委托给 DualPivotQuicksort.sort 方法实现
 参数包括：数组本身、起始偏移量（这里是0）、排序的起始索引和结束索引

 public final class Arrays类中的sort方法源码:
 public static void sort(int[] a, int fromIndex, int toIndex) {
        rangeCheck(a.length, fromIndex, toIndex);
        DualPivotQuicksort.sort(a, 0, fromIndex, toIndex);
    }

static void rangeCheck(int arrayLength, int fromIndex, int toIndex) {
        if (fromIndex > toIndex) {
            throw new IllegalArgumentException(
                "fromIndex(" + fromIndex + ") > toIndex(" + toIndex + ")");
        }
        if (fromIndex < 0) {
            throw new ArrayIndexOutOfBoundsException(fromIndex);
        }
        if (toIndex > arrayLength) {
            throw new ArrayIndexOutOfBoundsException(toIndex);
        }
    }
- arrayLength : 数组的总长度
- fromIndex : 操作的起始索引（包含）
- toIndex : 操作的结束索引（不包含）

rangeCheck 方法确实主要用于验证数组操作的索引范围，但它的调用场景比你想象的更广：

显式指定范围时直接调用
   当你调用 Arrays.sort(arr, fromIndex, toIndex) 这种带范围参数的方法时，会 直接调用 rangeCheck 进行验证
   这就是你看到的源码中的调用方式
调用无参sort()时也会间接调用
   当你调用无参的 Arrays.sort(arr) 方法时，它内部会 间接调用 带范围的sort方法
   具体来说，无参sort方法的实现通常是：

public static void sort(int[] a) {
    sort(a, 0, a.length);  // 调用带范围的sort方法，范围是整个数组
}
    因此，即使你没有显式指定范围， rangeCheck 仍然会被调用，只是验证的是0到数组长度的范围

static void sort(int[] a, int parallelism, int low, int high) {
这段代码的主要职责是 决定使用并行排序还是串行排序
        int size = high - low;//计算需要排序的数组片段大小

        if (parallelism > 1 && size > MIN_PARALLEL_SORT_SIZE) {
        //如果并行度大于1且数组大小超过最小并行排序阈值
            int depth = getDepth(parallelism, size >> 12);
            int[] b = depth == 0 ? null : new int[size];
            new Sorter(null, a, b, low, size, low, depth).invoke();
            //用并行排序策略（通过 Sorter 类
        } else {
            sort(null, a, 0, low, high);//否则使用普通串行排序（调用另一个 sort 重载方法）
        }
}
* */
        System.out.println("排序后：" + Arrays.toString(arr));
    }

    @Test
    public void test3() {
        Student[] arr = new Student[3];
        arr[0] = new Student(2, "张三", 89, 23);
        arr[1] = new Student(1, "李四", 100, 24);
        arr[2] = new Student(3, "王五", 90, 23);

        //按照id排序
        Arrays.sort(arr);
        //在Arrays.sort方法内部，它调用了元素的compareTo方法来比较两个元素对象的大小
        //在这个方法内部，会有一个操作 将arr[i]转型为Comparable接口类型，然后调用compareTo方法
        System.out.println("1");
        System.out.println(Arrays.toString(arr));
        System.out.println("1");
        //按照成绩排序
        //需要定制比较规则，找Comparator接口，用这个接口的compare方法
        Comparator c = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Student s1 = (Student) o1;
                Student s2 = (Student) o2;
                return Integer.compare(s1.getScore(), s2.getScore());
            }
        };
        Arrays.sort(arr, c);
        //在Arrays.sort（参数1，参数2）方法内部，一定有调用c.compare(元素1，元素2)
        //因为上面的匿名内部类重写了compare方法，所以sort方法内部调用的compare方法就是咱们重写的这个代码
        System.out.println(Arrays.toString(arr));

        //按照姓名排序
        Comparator nameComparator = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Student s1 = (Student) o1;
                Student s2 = (Student) o2;
                return s1.getName().compareTo(s2.getName());
                //s1.getName()是String类型，String类实现了Comparable接口
            }
        };
        Arrays.sort(arr, nameComparator);
        System.out.println(Arrays.toString(arr));
    }

    @Test
    public void test4() {
        Student[] arr = new Student[3];
        arr[0] = new Student(2, "zhangsan", 89, 23);
        arr[1] = new Student(1, "lisi", 100, 24);
        arr[2] = new Student(3, "wangwu", 90, 23);
        //按照姓名排序
        Comparator nameComparator = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Student s1 = (Student) o1;
                Student s2 = (Student) o2;
                return s1.getName().compareTo(s2.getName());
                //s1.getName()是String类型，String类实现了Comparable接口
                //按照字符串中每一个字符的编码值，先比第1个字符，如果不相同，就按第1个字符的编码值排序，如果第1个字符相同，就看第2个
            }
        };
        Arrays.sort(arr, nameComparator);
        System.out.println(Arrays.toString(arr));
    }

    @Test
    public void test5() {
        Student[] arr = new Student[3];
        arr[0] = new Student(2, "张三", 89, 23);
        arr[1] = new Student(1, "柴林燕", 100, 24);
        arr[2] = new Student(3, "孙浩伟", 90, 23);
        //按照姓名排序
        /*
        在java.text包下有一个Collator
        Collator 类执行区分语言环境的 String 比较。它实现了Comparator接口

         */
        Comparator nameComparator = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Student s1 = (Student) o1;
                Student s2 = (Student) o2;
                Collator collator = Collator.getInstance(Locale.CHINA);
                //Locale.CHINA  这是将语言环境设置为中文环境的意思，用于中文的字符串比较
//Collator类执行区域设置敏感String比较。 您使用此类来构建自然语言文本的搜索和排序例程
                /*
 以下示例显示如何使用默认语言环境的Collator比较两个字符串。

 // Compare two strings in the default locale
 Collator myCollator = Collator.getInstance();
 if( myCollator.compare("abc", "ABC") < 0 )
     System.out.println("abc is less than ABC");
 else
     System.out.println("abc is greater than or equal to ABC");
 */
                return collator.compare(s1.getName(), s2.getName());

            }
        };
        Arrays.sort(arr, nameComparator);
        System.out.println(Arrays.toString(arr));
    }

    @Test
    public void test6() {
        int[] arr = {2, 5, 8, 9, 12, 34};//有序数组

        int target = 6;
        int index = Arrays.binarySearch(arr, target);
        System.out.println("index = " + index);
        //index = -3
        //不存在时返回的结果是 -插入点-1
        //插入点是指如果把这个target插入到现在的数组中，应该在哪里

        int insertIndex = Math.abs(index + 1);
        System.out.println("insertIndex = " + insertIndex);

        target = 12;
        index = Arrays.binarySearch(arr, target);
        System.out.println("index = " + index);
        //index = 4
        //存在返回正常的下标
    }

    @Test
    public void test7(){
        Student[] arr = new Student[3];
        arr[0] = new Student(1, "张三", 89, 23);
        arr[1] = new Student(3, "柴林燕", 100, 24);
        arr[2] = new Student(4, "孙浩伟", 90, 23);

        Student s = new Student(2,"熊二",85,25);

        //按照id大小比较来确定元素的位置，因为Student的compareTo方法是按照id比较大小
        int index = Arrays.binarySearch(arr, s);
        System.out.println(index);
    }

    @Test
    public void test8(){
        Student[] arr = new Student[3];
        arr[0] = new Student(3, "张三", 89, 23);
        arr[1] = new Student(1, "柴林燕", 90, 24);
        arr[2] = new Student(4, "孙浩伟", 100, 23);

        Student s = new Student(2,"熊二",85,25);

        //按照成绩确定元素位置
        Comparator c = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Student s1 = (Student) o1;
                Student s2 = (Student) o2;
                return Integer.compare(s1.getScore(), s2.getScore());
            }
        };
        int index = Arrays.binarySearch(arr, s, c);
        System.out.println(index);//-1
    }

    @Test
    public void test9(){
        int[] arr = {2, 5, 8, 9, 12, 34};

        //复制数组
        int[] newArr1 = Arrays.copyOf(arr, arr.length);
        int[] newArr2 = Arrays.copyOf(arr, arr.length / 2);
        int[] newArr3 = Arrays.copyOf(arr, arr.length * 2);
        System.out.println(Arrays.toString(newArr1));//[2, 5, 8, 9, 12, 34]
        System.out.println(Arrays.toString(newArr2));//[2, 5, 8]
        System.out.println(Arrays.toString(newArr3));//[2, 5, 8, 9, 12, 34, 0, 0, 0, 0, 0, 0]
    }

    @Test
    public void test10(){
        int[] arr = {2, 5, 8, 9, 12, 34};

        //默认Arrays的copyOf实现复制数组
        int[] newArr1 = MyArrays.copyOf(arr, arr.length);
        int[] newArr2 = MyArrays.copyOf(arr, arr.length / 2);
        int[] newArr3 = MyArrays.copyOf(arr, arr.length * 2);
        System.out.println(Arrays.toString(newArr1));//[2, 5, 8, 9, 12, 34]
        System.out.println(Arrays.toString(newArr2));//[2, 5, 8]
        System.out.println(Arrays.toString(newArr3));//[2, 5, 8, 9, 12, 34, 0, 0, 0, 0, 0, 0]
    }

    @Test
    public void test11(){
        int[] arr = {2, 5, 8, 9, 12, 34};

        //复制arr[2] ~ arr[4] 的元素
        //在Java的方法中如果传入[a,b)两个下标，遵循左闭右开的原则，即含左不含右
        int[] newArr = Arrays.copyOfRange(arr, 2, 5);
        System.out.println(Arrays.toString(newArr));
    }

    @Test
    public void test12(){
        int[] arr = {2, 5, 8, 9, 12, 34};
        int[] newArr = {2, 5, 8, 9, 12, 35};

        System.out.println(Arrays.equals(arr, newArr));
    }

    @Test
    public void test13(){
        int[] arr = new int[5];//元素默认值是0
        Arrays.fill(arr, 1);
        System.out.println(Arrays.toString(arr));
    }
}
