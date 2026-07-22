"""
    该案例分析全排列的执行过程
"""
def permute(nums):
    result = []

    def backtrack(start):
        # 到达末尾，将此时排列结果添加到最终结果中
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            # 选取当前位置的元素：将要选取的元素与此位置的元素互换
            if start != i:
                nums[start], nums[i] = nums[i], nums[start]
            # 递归处理下一个位置的元素
            backtrack(start + 1)
            # 回溯，恢复原始数组
            if start != i:
                nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


print(permute([1, 2, 3]))