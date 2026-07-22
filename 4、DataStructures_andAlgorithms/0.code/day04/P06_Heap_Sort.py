"""
    该案例演示了堆排序
"""
#arr	需要进行堆化操作的序列
#n		序列中元素的个数
#i		当前需要进行堆化操作的子树的根节点索引
def heapify(arr, n, i):
    """堆化"""
    largest = i  # 最大节点指向父节点
    left = 2 * i + 1  # 左子节点
    right = 2 * i + 2  # 右子节点
    # 如果左子节点大于父节点,最大节点指向左子节点
    if left < n and arr[left] > arr[largest]:
        largest = left
    # 如果右子节点大于当前最大节点，最大节点指向右子节点
    if right < n and arr[right] > arr[largest]:
        largest = right
    # 如果最大节点不是父节点，则交换并递归堆化
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    """堆排序"""
    n = len(arr)
    # 构建大顶堆 # n//2–1获取最后一个非叶子节点的索引
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # 依次将堆顶元素放在末尾，并重新堆化
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
arr = [3,1,5,4,2]
sorted_arr = heap_sort(arr)
print("排序后的数组:", sorted_arr)
