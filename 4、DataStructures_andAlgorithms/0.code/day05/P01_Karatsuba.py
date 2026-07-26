"""
    该案例演示了卡拉楚巴算法
"""
def karatsuba(x, y):
    """卡拉楚巴算法"""
    # 将 x 和 y 转换为字符串
    x_str, y_str = str(x), str(y)
    n = max(len(x_str), len(y_str))

    # 如果存在负数，将其转换为正数再调用 karatsuba
    if x_str[0] == "-":
        return -karatsuba(-x, y)
    if y_str[0] == "-":
        return -karatsuba(x, -y)

    # 如果只剩1位则返回乘积
    if n == 1:
        return x * y

    # 确保数字长度一致
    x_str = x_str.zfill(n)  #zfill(n) 是字符串方法， 在字符串左侧填充0 ，使其达到长度n
    y_str = y_str.zfill(n)

    # 计算分割点
    m = n // 2

    # 将数字划分为高位部分和低位部分
    high1, low1 = int(x_str[:-m]), int(x_str[-m:])  #从倒数第m位开始，-m是负索引，从-1开始，这里就是从后面开始取
    high2, low2 = int(y_str[:-m]), int(y_str[-m:])

    # 令z0 = A0×B0
    # 令z1 = (A1 + A0)×(B1 + B0)
    # 令z2 = A1×B1

    # 递归调用 karatsuba
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return pow(10, 2 * m) * z2 + pow(10, m) * (z1 - z2 - z0) + z0

