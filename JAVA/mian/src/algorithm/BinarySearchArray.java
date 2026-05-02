package algorithm;
//二分法
public class BinarySearchArray {

// 迭代版二分查找
    public static int binarySearch(int[] arr, int target) {
        // 边界检查
        if (arr == null || arr.length == 0) {
            return -1;
        }

        int left = 0;                  // 左指针，初始指向数组第一个元素
        int right = arr.length - 1;    // 右指针，初始指向数组最后一个元素

        // 当左指针 <= 右指针时，继续查找
        while (left <= right) {
            // 计算中间位置（避免溢出：等价于(left + right)/2，但更安全）
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                return mid;  // 找到目标，返回索引
            } else if (arr[mid] < target) {
                left = mid + 1;  // 目标在右半部分，移动左指针
            } else {
                right = mid - 1; // 目标在左半部分，移动右指针
            }
        }

        return -1;  // 未找到目标，返回-1
    }

    // 递归版二分查找  ,并不比迭代版二分法计算快，且空间的消耗更大，为O(log n)
    public static int binarySearchRecursive(int[] arr, int target, int left, int right) {
        // 边界检查：未找到目标
        if (left > right) {
            return -1;
        }

        // 计算中间位置
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;  // 找到目标，返回索引
        } else if (arr[mid] < target) {
            // 递归查找右半部分
            return binarySearchRecursive(arr, target, mid + 1, right);
        } else {
            // 递归查找左半部分
            return binarySearchRecursive(arr, target, left, mid - 1);
        }
    }

    // 测试
    public static void main(String[] args) {
        int[] sortedArray = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;

        // 测试迭代版
        int result1 = binarySearch(sortedArray, target);
        System.out.println("迭代版查找结果：" + (result1 != -1 ? "找到，索引为" + result1 : "未找到"));

        // 测试递归版
        int result2 = binarySearchRecursive(sortedArray, target, 0, sortedArray.length - 1);
        System.out.println("递归版查找结果：" + (result2 != -1 ? "找到，索引为" + result2 : "未找到"));
    }
}
