"""
    该案例演示了选择排序
"""
def select_sort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

list1 = [3,1,5,4,2]
select_sort(list1)
print(list1)