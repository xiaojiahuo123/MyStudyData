"""
    该案例演示了快速排序
"""
def partition(nums, left, right):
    """选择基准并按基准划分"""
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left

def quick_sort(nums, left, right):
    """快速排序"""
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)

list1 = [3,1,5,4,2]
quick_sort(list1,0,len(list1)-1)
print(list1)