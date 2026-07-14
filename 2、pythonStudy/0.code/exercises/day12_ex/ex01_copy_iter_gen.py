"""
Day12 练习1 - 浅拷贝/深拷贝、迭代器与生成器
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
# 预测: shallow 的内容是什么? shallow[0] is original[0] 为何为 True?
# ____[[99, 2], [3, 4]]，original是一个列表，并且其中的子类对象也是列表，是引用类型的，因此浅拷贝得到的shallow中的子对象和原本的original指向相同的地址
#所以shallow[0] is original[0] 为 True

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
# 预测: deep 的内容是什么? deep[0] is original2[0] 为何为 False?
# ____[[1, 2], [3, 4]]
#深拷贝是完全的拷贝，列表中的子对象也是创建了新的，deep和原本的original2指向不同的地址

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
# 预测: 为什么 t1 is t2 为 True? deepcopy 后 t1 is t3 为 False?
# ____浅拷贝的原理是子类对象指向同一地址，Python 认为元组本身是不可变类型（不能增删元素），所以浅拷贝没有意义，直接返回原对象。即使内部有可变元素，Python 也不管。
# 深拷贝是创建的新的对象

# ----- 题4: 非容器类型的拷贝 [必做] -----
# 知识点: 不可变非容器类型(int, str, float)调用 copy.copy 返回原对象
print("\n----- 题4: 非容器类型的拷贝 -----")

a = 42
b = copy.copy(a)
c = "hello"
d = copy.copy(c)

print(f"a is b = {a is b}")
print(f"c is d = {c is d}")
# 预测: a is b 和 c is d 各为何为 True?
# ____不可变类型的浅拷贝没有意义，所以直接俄返回原本的值

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
# 预测: 每次 next(it) 分别输出什么? 为何最终抛出 StopIteration?
# ____10，20，30，最后抛出StopIteration是因为越界了，原本的it只到第三个


# ============================================================
#                    第二部分: 进阶题
# ============================================================
print("\n" + "=" * 50)
print("        第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 生成器表达式 vs 列表推导式 [必做] -----
# 知识点: 生成器表达式(generator expression)惰性求值，不立即生成全部元素
print("\n----- 题6: 生成器表达式 vs 列表推导式 -----")

list_comp = [x ** 2 for x in range(5)]  # 列表推导式
gen_expr = (x ** 2 for x in range(5))  # 生成器表达式

print(f"type(list_comp) = {type(list_comp)}")
print(f"type(gen_expr)  = {type(gen_expr)}")
print(f"list_comp = {list_comp}")
print(f"list(gen_expr) = {list(gen_expr)}")
# 预测: type(gen_expr) 的类型是什么? 直接 print(gen_expr) 会显示什么?
# ____是生成器对象，直接print(gen_expr)不会输出数值而是将生成器及其地址打印出来，用list包裹之后才会按照列表的格式打印输出

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
print(f"第1次 next: {next(gen)}") # 3，在输出3之前输出"countdown 开始"
print(f"第2次 next: {next(gen)}") # 2
print(f"第3次 next: {next(gen)}") # 1

try:
    next(gen) # "发射!"
except StopIteration:
    print("StopIteration 被捕获")
# 预测: "countdown 开始" 和 "发射!" 分别在什么时候打印? 完整输出顺序?
# ____在输出3之前输出"countdown 开始"，因为这个时候刚进入countdown()函数，还没有进入while循环
#发射在try中打印，因为这个时候n执行n -= 1,n变为0，不满足while条件，yield无法暂停直接返回值，执行最后的发射

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
print(f"初始化 next(): {next(acc)}") # 0
print(f"send(10): {acc.send(10)}") # 10
print(f"send(20): {acc.send(20)}") # 30
print(f"send(30): {acc.send(30)}") # 60
# 预测: 每一步输出什么? 为什么第一次必须调用 next() 而不是 send()?
# ____因为生成器刚创建时， 还没有执行到任何 yield ，没有地方接收 send() 发送的值

# ----- 题9: 自定义迭代器类 [必做] -----
# 知识点: 实现 __iter__() 和 __next__() 协议即可创建自定义迭代器
print("\n----- 题9: 自定义迭代器类 -----")
# TODO: 实现一个 Countdown 类，从 start 倒数到 1
# 要求:
#   - 构造函数接收 start 参数
#   - __iter__() 返回 self
#   - __next__() 返回当前值并递减，到 0 时抛出 StopIteration

class Countdown:
    #index = 0
    # TODO: 实现 __init__, __iter__, __next__
    def __init__(self,data):
        self.data = data
        self.index = data + 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index - 1 == 0:
            raise StopIteration
        self.index -= 1
        return self.index


# 测试代码 (取消注释以验证):
for num in Countdown(5):
    print(num, end=" ")
# 期望输出: 5 4 3 2 1


# ============================================================
#                    第三部分: 深入理解题
# ============================================================
print("\n" + "=" * 50)
print("        第三部分: 深入理解题")
print("=" * 50)

# ----- 题10: 生成器实现斐波那契数列 [选做] -----
# 知识点: 用生成器无限生成斐波那契数，体会惰性求值(lazy evaluation)
print("\n----- 题10: 生成器实现斐波那契数列 -----")
# TODO: 实现 fibonacci() 生成器函数，无限生成斐波那契数
# 提示: 使用 a, b = b, a + b 同时更新

def fibonacci():
    """无限生成斐波那契数: 0, 1, 1, 2, 3, 5, 8, ..."""
    # TODO: 实现斐波那契生成器
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
    pass

# 测试代码 (取消注释以验证):
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
# 期望输出: 0 1 1 2 3 5 8 13 21 34


# ----- 题11: 迭代器惰性求值的内存优势分析 [选做] -----
# 知识点: 迭代器(iterator)按需生成 vs 列表一次性存储
print("\n----- 题11: 迭代器惰性求值的内存优势分析 -----")
import sys

data_list = [x ** 2 for x in range(100_000)]
data_gen = (x ** 2 for x in range(100_000))

print(f"列表内存占用: {sys.getsizeof(data_list)} 字节")
print(f"生成器内存占用: {sys.getsizeof(data_gen)} 字节")
# 思考:
# 1. 为什么生成器的内存占用远小于列表?
# 2. 什么场景必须用列表而不能用生成器?
# ____因为生成器现在没有被调用，只是一个生成器对象，他是根据调用来开辟内存的
# 我必须获取到完整的数据而不能按需生成的时候，比如一个用户搜索查询的接口，用户需要搜索后得出所有信息，不能用生成器


# ----- 题12: 调试修复 - 有 Bug 的迭代器 [选做] -----
# 知识点: 自定义迭代器的常见错误与调试
print("\n----- 题12: 调试修复 - 有 Bug 的迭代器 -----")

# BUG: 以下代码想实现步长为 2 的迭代器，但结果不正确
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
        self.index += 2  # BUG: 应该加 self.step 而不是 1
        # 实现步长为2，应该每次返回的元素索引都是 +2，这里使用了 self.index += 1，首先是步长变为1
        return value

# 测试
print("StepIterator [1,2,3,4,5,6], step=2:")
print(list(StepIterator([1, 2, 3, 4, 5, 6], step=2)))
# 期望输出: [1, 3, 5]
# 实际输出: [1, 2, 3, 4, 5, 6]
# 请找出 BUG 并修复
# ____