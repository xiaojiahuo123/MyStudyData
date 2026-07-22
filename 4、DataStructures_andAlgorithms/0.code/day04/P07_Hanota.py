"""
    P01_Hanota
"""
def print_abc():
    """打印3个柱子"""
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("~~~~~~~~~~~~~~")


def hanota(n, source, target, buffer):
    # 只有一个盘子时，直接从源柱子移动到目标柱子
    if n == 1:
        s = source.copy()
        item = source.pop()
        target.append(item)
        print(f"{s}的{item}移动到了{target}")
        return

    # 1. 将 n-1 个盘子从源柱子移动到缓冲柱子
    hanota(n - 1, source, buffer, target)
    # print_abc()

    # 2. 将第 n 个盘子从源柱子移动到目标柱子
    hanota(1, source, target, buffer)
    # print_abc()

    # 3. 将 n-1 个盘子从缓冲柱子移动到目标柱子
    hanota(n - 1, buffer, target, source)
    print_abc()

if __name__ == "__main__":
    n = 3
    a = list(range(n, 0, -1))
    b = []
    c = []
    hanota(n, a, c, b)
