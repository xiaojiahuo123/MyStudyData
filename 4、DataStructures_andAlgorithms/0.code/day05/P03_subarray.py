"""
    该案例演示了求出数组连续累加和最大的子数组
"""
def max_subarray(nums):
    result, f = nums[0], 0
    for i in nums:
        # 连续子数组之和若小于0，则中断连续
        if f < 0:
            f = 0
        # 累加连续子数组之和
        f += i
        # 更新最大值
        if result < f:
            result = f
    return result
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
