"""
    该案例演示了插入排序
"""
def insert_sort(nums):
# 是后一位元素和之前的元素相互比较，如果后一位元素小于前一位元素，就交换位置
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] >= nums[j - 1]:
                break
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

list1 = [3,1,5,4,2]
insert_sort(list1)
print(list1)