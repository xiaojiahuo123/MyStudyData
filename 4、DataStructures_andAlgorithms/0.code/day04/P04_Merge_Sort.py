"""
    该案例演示了归并排序
"""
def merge(left, right):
    """合并两个已排序的数组"""
    merged = []
    i = j = 0
    # 比较两个子数组的元素，按升序放入 merged 数组
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # 将数组中剩余元素加入 merged
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def merge_sort(arr):
    """归并排序"""
    # 数组长度为1时，不再分割
    if len(arr) <= 1:
        return arr
    # 分割数组
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 合并已排序的子数组
    return merge(left, right)

list1 = [3,1,4,2]
print(merge_sort(list1))