"""
    该案例演示了大O表示法
"""
import time


# 提供一个函数，完成对list中的元素进行求和
# 通过执行绝对时间衡量算法好坏
def sum(nums):
    start_time = time.time()
    res = 0
    i = -1
    while (i:=i+1) < len(nums):
        res += nums[i]

    end_time = time.time()
    print(f"总耗时:{end_time-start_time}")
    return res

print(sum([x for x in range(10000000)]))

"""
def sum(nums):
    res = 0 # 1次赋值操作
    i = -1  # 1次赋值操作
    while (i:=i+1) < len(nums): #    # n + 1次运算  、n + 1次赋值、 n + 1次比较
        res += nums[i]    # n次运算    n次赋值

    return res
#总计执行多少次操作：    T(n) = 5n + 5   对n条数据进行处理，需要的执行时间单元是5n + 5
# O(n)
"""
def permute(nums):
    result = []

    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
        remaining = nums[:i] + nums[i + 1 :]
        for perm in permute(remaining):
            result.append([nums[i]] + perm)

    return result


print(permute([1, 2, 3,4]))