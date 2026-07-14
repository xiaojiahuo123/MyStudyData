"""
Day12 练习1 - 浅拷贝/深拷贝、迭代器与生成器 (参考答案)
由浅入深掌握 copy 模块、迭代器协议、生成器原理

参考源码: day12/P01_Copy.py
         day12/P02_Iterator.py
         day12/P03_Generator.py
版本: v1.0
最后更新: 2026-07-13
"""

import copy

# ============================================================
#                      第一部分: 基础题
# ============================================================
print("=" * 50)
print("        第一部分: 基础题")
print("=" * 50)

# ----- 题1: 浅拷贝预测 [必做] -----
# 知识点: 浅拷贝(shallow copy)只复制外层对象，内层对象仍共享引用
# 预测以下代码中 shallow 的内容，以及 is 比较的结果
print("\n----- 题1: 浅拷贝预测 -----")

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

original[0][0] = 99
original.append([5, 6])

print(f"original = {original}")
print(f"shallow  = {shallow}")
print(f"shallow[0] is original[0] = {shallow[0] is original[0]}")
# ✅ 答案: shallow = [[99, 2], [3, 4]]
#   浅拷贝只复制外层列表，内层的 [1,2] 和 [3,4] 仍是同一个对象
#   因此修改 original[0][0] = 99 会影响 shallow[0]
#   但 append 的 [5, 6] 只添加到 original，不影响 shallow
#   shallow[0] is original[0] 为 True，因为内层列表共享引用

# ----- 题2: 深拷贝预测 [必做] -----
# 知识点: 深拷贝(deep copy)递归复制所有嵌套对象，与原对象完全独立
print("\n----- 题2: 深拷贝预测 -----")

original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)

original2[0][0] = 99
original2.append([5, 6])

print(f"original2 = {original2}")
print(f"deep      = {deep}")
print(f"deep[0] is original2[0] = {deep[0] is original2[0]}")
# ✅ 答案: deep = [[1, 2], [3, 4]]
#   深拷贝递归复制了所有嵌套对象，deep 与 original2 完全独立
#   修改 original2 不会影响 deep
#   deep[0] is original2[0] 为 False，因为内层列表也是独立副本

# ----- 题3: 元组拷贝特殊性 [必做] -----
# 知识点: 不可变容器(tuple)包含可变元素时，copy.copy 返回同一对象
print("\n----- 题3: 元组拷贝特殊性 -----")

t1 = ([1, 2], [3, 4])
t2 = copy.copy(t1)
t3 = copy.deepcopy(t1)

print(f"t1 is t2       = {t1 is t2}")
print(f"t1[0] is t2[0] = {t1[0] is t2[0]}")
print(f"t1 is t3       = {t1 is t3}")
print(f"t1[0] is t3[0] = {t1[0] is t3[0]}")
# ✅ 答案:
#   t1 is t2 = True: 元组是不可变对象，copy.copy 认为没有复制的必要，直接返回自身
#   t1[0] is t2[0] = True: 同理，t1 和 t2 是同一个对象
#   t1 is t3 = False: deepcopy 递归复制了元组及其内部的可变列表
#   t1[0] is t3[0] = False: deepcopy 创建了新的列表对象

# ----- 题4: 非容器类型的拷贝 [必做] -----
# 知识点: 不可变非容器类型(int, str, float)调用 copy.copy 返回原对象
print("\n----- 题4: 非容器类型的拷贝 -----")

a = 42
b = copy.copy(a)
c = "hello"
d = copy.copy(c)

print(f"a is b = {a is b}")
print(f"c is d = {c is d}")
# ✅ 答案:
#   a is b = True: int 是不可变非容器类型，copy.copy 直接返回原对象
#   c is d = True: str 也是不可变非容器类型，同理
#   原因: 不可变对象不存在被意外修改的风险，无需复制

# ----- 题5: iter() 和 next() 基本用法 [必做] -----
# 知识点: 迭代器协议(iterator protocol)——iter() 获取迭代器, next() 逐个取值
print("\n----- 题5: iter() 和 next() 基本用法 -----")

nums = [10, 20, 30]
it = iter(nums)

print(f"next(it) = {next(it)}")
print(f"next(it) = {next(it)}")
print(f"next(it) = {next(it)}")

try:
    next(it)
except StopIteration:
    print("捕获到 StopIteration")
# ✅ 答案:
#   next(it) = 10
#   next(it) = 20
#   next(it) = 30
#   捕获到 StopIteration
#   原因: iter() 返回列表的迭代器对象，next() 每次调用返回下一个元素
#   当所有元素耗尽后，__next__() 抛出 StopIteration 表示迭代结束


# ============================================================
#                    第二部分: 进阶题
# ============================================================
print("\n" + "=" * 50)
print("        第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 生成器表达式 vs 列表推导式 [必做] -----
# 知识点: 生成器表达式(generator expression)惰性求值，不立即生成全部元素
print("\n----- 题6: 生成器表达式 vs 列表推导式 -----")

list_comp = [x ** 2 for x in range(5)]
gen_expr = (x ** 2 for x in range(5))

print(f"type(list_comp) = {type(list_comp)}")
print(f"type(gen_expr)  = {type(gen_expr)}")
print(f"list_comp = {list_comp}")
print(f"list(gen_expr) = {list(gen_expr)}")
# ✅ 答案:
#   type(list_comp) = <class 'list'>
#   type(gen_expr) = <class 'generator'>
#   直接 print(gen_expr) 会显示类似 <generator object <genexpr> at 0x...> 的地址
#   因为生成器是惰性的，不会立即计算元素，只有在迭代时才逐个生成

# ----- 题7: yield 执行流程预测 [必做] -----
# 知识点: yield 暂停函数执行并保存状态，下次 next() 从暂停处恢复
print("\n----- 题7: yield 执行流程预测 -----")

def countdown(n):
    print(f">>> countdown 开始, n={n}")
    while n > 0:
        yield n
        n -= 1
    print(">>> 发射!")

gen = countdown(3)
print(f"第1次 next: {next(gen)}")
print(f"第2次 next: {next(gen)}")
print(f"第3次 next: {next(gen)}")

try:
    next(gen)
except StopIteration:
    print("StopIteration 被捕获")
# ✅ 答案: 完整输出顺序:
#   >>> countdown 开始, n=3     (首次 next 触发函数执行到第一个 yield)
#   第1次 next: 3               (yield 3 后暂停)
#   第2次 next: 2               (恢复后 n=2, yield 2)
#   第3次 next: 1               (恢复后 n=1, yield 1)
#   >>> 发射!                   (恢复后 n=0, while 条件为 False, 打印后函数结束)
#   StopIteration 被捕获        (函数结束自动触发 StopIteration)
#
#   关键: "countdown 开始" 在第一次 next() 时打印
#   "发射!" 在第四次 next() 时(while 退出后)打印，然后抛出 StopIteration

# ----- 题8: send() 方法 [必做] -----
# 知识点: send(value) 向生成器发送值，该值成为 yield 表达式的返回值
print("\n----- 题8: send() 方法 -----")

def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
print(f"初始化 next(): {next(acc)}")
print(f"send(10): {acc.send(10)}")
print(f"send(20): {acc.send(20)}")
print(f"send(30): {acc.send(30)}")
# ✅ 答案:
#   初始化 next(): 0        (运行到 yield total, 此时 total=0)
#   send(10): 10            (value=10, total=0+10=10, yield 10)
#   send(20): 30            (value=20, total=10+20=30, yield 30)
#   send(30): 60            (value=30, total=30+30=60, yield 60)
#
#   为什么第一次必须 next():
#   因为生成器启动时还没执行到 yield 语句，没有暂停点来接收 send 的值
#   首次 send(None) 等价于 next()，但语义上用 next() 更清晰

# ----- 题9: 自定义迭代器类 [必做] -----
# 知识点: 实现 __iter__() 和 __next__() 协议即可创建自定义迭代器
print("\n----- 题9: 自定义迭代器类 -----")
# 参考实现: Countdown 类

class Countdown:
    """从 start 倒数到 1 的迭代器"""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# 测试
print("Countdown(5):", end=" ")
for num in Countdown(5):
    print(num, end=" ")
print()
# 输出: 5 4 3 2 1


# ============================================================
#                    第三部分: 深入理解题
# ============================================================
print("\n" + "=" * 50)
print("        第三部分: 深入理解题")
print("=" * 50)

# ----- 题10: 生成器实现斐波那契数列 [选做] -----
# 知识点: 用生成器无限生成斐波那契数，体会惰性求值(lazy evaluation)
print("\n----- 题10: 生成器实现斐波那契数列 -----")
# 参考实现: fibonacci 生成器

def fibonacci():
    """无限生成斐波那契数: 0, 1, 1, 2, 3, 5, 8, ..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 测试
fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(f"前10个斐波那契数: {first_10}")
# 输出: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ----- 题11: 迭代器惰性求值的内存优势分析 [选做] -----
# 知识点: 迭代器(iterator)按需生成 vs 列表一次性存储
print("\n----- 题11: 迭代器惰性求值的内存优势分析 -----")
import sys

data_list = [x ** 2 for x in range(100_000)]
data_gen = (x ** 2 for x in range(100_000))

print(f"列表内存占用: {sys.getsizeof(data_list)} 字节")
print(f"生成器内存占用: {sys.getsizeof(data_gen)} 字节")
# ✅ 答案:
#   1. 列表一次性将所有 100000 个元素存入内存，占用约 800KB+
#      生成器只存储生成器对象的状态(函数帧+局部变量)，占用约 200 字节
#      每次 next() 时才计算并返回一个值，用完即丢
#
#   2. 必须用列表的场景:
#      - 需要随机访问(如 data[5000])
#      - 需要多次遍历同一数据
#      - 需要知道数据长度(len)
#      适合用生成器的场景:
#      - 只需顺序遍历一次
#      - 数据量极大或无限
#      - 链式处理(管道模式)


# ----- 题12: 调试修复 - 有 Bug 的迭代器 [选做] -----
# 知识点: 自定义迭代器的常见错误与调试
print("\n----- 题12: 调试修复 - 有 Bug 的迭代器 -----")

# 修复后的 StepIterator
class StepIterator:
    """从数据中按指定步长取值"""

    def __init__(self, data, step=2):
        self.data = data
        self.step = step
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += self.step  # 修复: 应该加 self.step 而不是 1
        return value

# 测试
print("StepIterator [1,2,3,4,5,6], step=2:")
print(list(StepIterator([1, 2, 3, 4, 5, 6], step=2)))
# 输出: [1, 3, 5]  ✅
#
# BUG 说明: 原代码 self.index += 1 每次只前进 1，忽略了 step 参数
# 修复: 改为 self.index += self.step，按指定步长前进