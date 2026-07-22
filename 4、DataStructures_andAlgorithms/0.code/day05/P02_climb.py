"""
    该案例演示了爬楼梯
"""
# def climb(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return climb(n - 1) + climb(n - 2)

def climb(n):
    pre = 1
    cur = 1
    for _ in range(1, n):
        pre, cur = cur, pre + cur
    return cur

print(climb(5))
