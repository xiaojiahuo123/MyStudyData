package day05_teacher_code.src;

import java.lang.reflect.Array;//案例需求：判断某个数组是否属于对称数组，即数组正序遍历和倒序遍历的结果是一样的。
//symmetry 对称
public class MyLianxi_04 {

    public static void main(String[] args) {
        String[] strArray1 = {"a", "b", "c", "b", "a"};
        String[] strArray2 = {"a", "b", "c", "d"};
        System.out.println("字符串数组1是否对称: " + isSymmetric(strArray1)); // true
        System.out.println("字符串数组2是否对称: " + isSymmetric(strArray2)); // false

        // 测试整数数组
        Integer[] intArray1 = {1, 2, 3, 2, 1};
        Integer[] intArray2 = {1, 2, 3, 4, 5};
        System.out.println("整数数组1是否对称: " + isSymmetric(intArray1)); // true
        System.out.println("整数数组2是否对称: " + isSymmetric(intArray2)); // false

        // 测试包含null的数组
        String[] nullArray = {"a", null, "a"};
        System.out.println("包含null的数组是否对称: " + isSymmetric(nullArray)); // true

        // 测试单元素数组
        Character[] charArray = {'x'};
        System.out.println("单元素数组是否对称: " + isSymmetric(charArray)); // true
    }

    /**
     * 判断任意类型数组是否对称
     * @param array 要检查的数组
     * @param <T> 数组元素的类型
     * @return 如果数组对称返回true，否则返回false
     */
    public static <T> boolean isSymmetric(T[] array) {
        // 处理空数组或长度为0的情况
        if (array == null) {
            throw new IllegalArgumentException("数组不能为null");
        }
        if (array.length <= 1) {
            return true; // 空数组或单个元素的数组视为对称
        }

        // 比较对称位置的元素
        int left = 0;
        int right = array.length - 1;

        while (left < right) {
            // 使用equals比较元素，处理null元素的情况
            if (!elementsEqual(array[left], array[right])) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

    /**
     * 比较两个元素是否相等，处理null的情况
     */
    private static <T> boolean elementsEqual(T a, T b) {
        if (a == b) {
            return true; // 包括两者都为null的情况
        }
        if (a == null || b == null) {
            return false; // 其中一个为null
        }
        return a.equals(b); // 都不为null时使用equals比较
    }
}

