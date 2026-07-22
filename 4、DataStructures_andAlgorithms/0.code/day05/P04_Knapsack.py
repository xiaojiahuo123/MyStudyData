"""
    该案例演示了0-1背包
"""
def knapsack(weights, values, W):
    n = len(weights)
    # 初始化二维数组dp，dp[i][j]表示前i个物品中，背包容量为j时的最大价值
    dp = [[0] * (W + 1) for _ in range(n)]

    # 每次增加一个可选物品，增加物品后遍历一次背包重量
    for i in range(n):
        for j in range(1, W + 1):
            # 如果当前物品放的进背包，进行比较
            if weights[i] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i] + dp[i - 1][j - weights[i]])
            # 如果当前物品放不进背包，使用上轮相同j的状态
            else:
                dp[i][j] = dp[i - 1][j]

            print(f"前{i + 1}个物品，背包容量为{j}时")
            for row in range(len(dp)):
                print(dp[row])

    return dp[n - 1][W]


if __name__ == "__main__":
    weights = [1, 2, 3]  # 物品的重量
    values = [3, 2, 6]  # 物品的价值
    W = 3  # 背包的最大容量
    print(knapsack(weights, values, W))
