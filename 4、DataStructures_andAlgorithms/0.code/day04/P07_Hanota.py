"""
    P01_Hanota
"""
def print_abc():
    """打印3个柱子"""
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("~~~~~~~~~~~~~~")


def hanota(n, source, target, buffer):  # n , a, c, b
    # 只有一个盘子时，直接从源柱子移动到目标柱子
    if n == 1:
        s = source.copy()
        item = source.pop()
        target.append(item)
        print(f"{s}的{item}移动到了{target}")
        return

    # 1. 将 n-1 个盘子从源柱子移动到缓冲柱子
    hanota(n - 1, source, buffer, target)  
    # 这里是将 n-1 个盘子从 source 移动到 buffer，b（缓冲柱子）作为递归的target
    # print_abc()

    # 2. 将第 n 个盘子从源柱子移动到目标柱子
    hanota(1, source, target, buffer)  # 上面的都移动到缓冲处buffer了，因为这个n=1，所以直接移动到目标柱子target
    # print_abc()

    # 3. 将 n-1 个盘子从缓冲柱子移动到目标柱子
    hanota(n - 1, buffer, target, source)
    # 再递归调用，进入hanota(n - 1, source, buffer, target)，最终到n = 1，
    print_abc()

if __name__ == "__main__":
    n = 3
    a = list(range(n, 0, -1))
    b = []
    c = []
    hanota(n, a, c, b)
