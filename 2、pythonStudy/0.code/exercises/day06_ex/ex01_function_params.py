"""
Day06 练习1 - 函数参数与参数传递
由浅入深掌握函数参数的各种用法及浅拷贝/深拷贝

参考源码: day06/P03_Func_Param.py
         day06/P04_Param_Pass.py
         day06/P05_Param_Pass_Type.py
         day06/P06_ChangeList.py
版本: v1.0
最后更新: 2026-06-14
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 必须参数与关键字参数 [必做] -----
# 知识点: 必须参数按位置匹配，关键字参数按名称匹配
# 预测以下代码的输出结果

def greet(name, msg):
    print(f"{name}, {msg}")

greet("Alice", "早上好")
greet(msg="下午好", name="Bob")
# Alice，早上好____（预测第1行输出）
# Bob,下午好____（预测第2行输出）

print()

# ----- 题2: 参数默认值 [必做] -----
# 知识点: 函数参数可以设置默认值，调用时可省略
# 预测以下代码的输出结果

def power(base, exp=2):
    return base ** exp

print(power(3))       # ____9
print(power(3, 3))    # ____27
print(power(2, 5))    # ____32

print()

# ----- 题3: 不定长参数 *args [必做] -----
# 知识点: 加了星号 * 的参数以元组形式接收未命名参数
# 预测以下代码的输出结果

def calc_sum(*args):
    print(f"args的类型: {type(args)}")
    print(f"args的值: {args}")
    return sum(args)

result = calc_sum(1, 2, 3, 4, 5)
print(f"求和结果: {result}")
# ____type class<tuple>
# ____(1,2,3,4,5)
# ____(15)

print()

# ----- 题4: 不定长参数 **kwargs [必做] -----
# 知识点: 加了双星号 ** 的参数以字典形式接收关键字参数
# 预测以下代码的输出结果

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=20, city="北京")
# ____name:"张三"
# age:20
# city:"北京"}

print()

# ----- 题5: 解包传参 [必做] -----
# 知识点: 使用 * 和 ** 对序列/字典进行解包传参
# 预测以下代码的输出结果

def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
info = {"a": 10, "b": 20, "c": 30}

print(add(*nums))       # ____6
print(add(**info))       # ____60

print()

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 参数传递 - 不可变对象 [必做] -----
# 知识点: 传递不可变对象(int/str/tuple)时，函数内修改不会影响外部变量
# 预测以下代码的输出结果

def modify_int(x):
    print(f"函数内修改前: x={x}, id={id(x)}")
    x = 100
    print(f"函数内修改后: x={x}, id={id(x)}")

a = 10
print(f"函数调用前: a={a}, id={id(a)}")
modify_int(a)
print(f"函数调用后: a={a}, id={id(a)}")
# ____10
# ____10
# ____100
# ____10

print()

# ----- 题7: 参数传递 - 可变对象 [必做] -----
# 知识点: 传递可变对象(list/dict)时，函数内修改元素会影响外部对象
# 预测以下代码的输出结果

def modify_list(lst):
    print(f"函数内修改前: {lst}, id={id(lst)}")
    lst.append(4)
    print(f"函数内修改后: {lst}, id={id(lst)}")

my_list = [1, 2, 3]
print(f"函数调用前: {my_list}, id={id(my_list)}")
modify_list(my_list)
print(f"函数调用后: {my_list}, id={id(my_list)}")
# ____[1,2,3]
# ____[1,2,3]
# ____[1,2,3,4]
# ____[1,2,3,4]

print()

# ----- 题8: 函数内重新赋值 vs 修改元素 [必做] -----
# 知识点: 函数内对参数重新赋值(=)不会影响外部变量，但修改元素会影响
# 预测以下代码的输出结果

def try_replace(lst):
    lst = [99, 100, 101]  # 重新赋值  重新赋值是会创建一个新的局部变量，所以赋值之后即使对列表进行操作，也只是操作的局部变量
    # lst.append(10)
    # lst.insert(1,100)
    print(f"函数内: {lst}")

def try_modify(lst):
    lst[0] = 99  # 修改元素
    print(f"函数内: {lst}")

list1 = [1, 2, 3]
try_replace(list1)
print(f"try_replace后: {list1}")  # ____[1,2,3]

list2 = [1, 2, 3]
try_modify(list2)
print(f"try_modify后: {list2}")   # ____[1,2,3]

print()

# ----- 题9: 带 * 的不定长参数的位置规则 [必做] -----
# 知识点: *args 后面的参数必须用关键字传参
# 预测以下代码能否正常运行，以及输出结果

def func(a, *args, b):
    print(f"a={a}, args={args}, b={b}")

func(1, 2, 3, 4, b = 5)
# ____1,(2,3,4),5

# 以下代码会报错吗？为什么？
# func(1, 2, 3, 4, 5)
# ____会，没有传入关键字参数b

print()

# ----- 题10: 浅拷贝与深拷贝 [必做] -----
# 知识点: 浅拷贝共享子对象，深拷贝完全独立
# 预测以下代码的输出结果

import copy

original = [1, [2, 3], 4]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[1][0] = 99
deep[1][1] = 88

print(f"original = {original}")  # ____[1, [99, 3], 4]
print(f"shallow  = {shallow}")   # ____[1, [99, 3], 4]
print(f"deep     = {deep}")      # ____[1, [2, 88], 4]
# copy()是浅拷贝，返回的新的对象的子对象仍然指向之前的子对象  ，  deepcopy()是深拷贝，返回的对象的子对象也是新创建的，所以修改的时候原本的列表的子对象不受影响
print()

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题11: 浅拷贝的多种方式 [选做] -----
# 知识点: 列表的 copy()、切片 [:]、list()、copy.copy() 都是浅拷贝
# 预测以下代码的输出结果

import copy

original = [[1, 2], [3, 4]]

c1 = original.copy()
c2 = original[:]
c3 = list(original)
c4 = copy.copy(original)

# 验证是否都是新对象
print(c1 is original)  # ____flase
print(c2 is original)  # ____flase

# 验证子对象是否共享
c1[0][0] = 999
print(f"original = {original}")  # ____[[999, 2], [3, 4]]
print(f"c1 = {c1}")              # ____[[999, 2], [3, 4]]

print()

# ----- 题12: 参数传递的本质 - 引用传递 [选做] -----
# 知识点: Python 的参数传递本质是"引用传递"（传递对象的引用）
# 预测以下代码的输出结果

def mystery(lst):
    lst += [4, 5]  # 注意: += 对列表是原地修改

data = [1, 2, 3]
mystery(data)
print(f"data = {data}")  # ____[1,2,3,4,5]

# 对比: 如果把 += 换成 = 呢？
def mystery2(lst):
    lst = lst + [4, 5]  # 注意: = 是重新赋值

data2 = [1, 2, 3]
mystery2(data2)
print(f"data2 = {data2}")  # ____[1, 2, 3]

print()

# ----- 题13: 函数返回多个值的本质 [选做] -----
# 知识点: 返回多个值实际上是返回一个元组
# 预测以下代码的输出结果

def get_info():
    return "张三", 20, "北京"

result = get_info()
print(f"result = {result}")       # ____("张三", 20, "北京")
print(f"type = {type(result)}")   # ____tuple

name, age, city = get_info()
print(f"name={name}, age={age}, city={city}")  # ____"张三", 20, "北京"

print()

# ----- 题14: 综合应用 - 设计一个安全的列表处理函数 [选做] -----
# 知识点: 综合运用深拷贝、函数参数、返回值
# 要求: 实现一个函数，接收嵌套列表，返回排序后的新列表，不修改原列表
# 提示: 需要用深拷贝来保护原数据

def safe_sort(nested_list):
    """对嵌套列表进行安全排序（不修改原列表）
    例如: 输入 [[3,1], [2,4], [1,3]]
    返回: [[1,3], [2,4], [3,1]]（按每个子列表的第一个元素排序）
    """
    nested_list_1 = copy.deepcopy(nested_list)
    print(f"nested_list_1 = {nested_list_1}")
    # countLst = 0
    # for item in nested_list_1:  # 题目的意思是列表中的元素按照自身的第一个元素的大小排序，我的做法是让列表中的子对象内部进行的排序，虽然也恰好一样但是不对
    #     item.sort()
    #     nested_list_1[countLst] = item
    #     countLst += 1
    nested_list_1.sort(key=lambda x: x[0])
    return nested_list_1
    #pass  # TODO: 学生实现

# 验证
test_data = [[3, 1], [2, 4], [1, 3]]
result = safe_sort(test_data)
print(f"原数据: {test_data}")    # 预期: [[3, 1], [2, 4], [1, 3]]（不变）
print(f"排序后: {result}")       # 预期: [[1, 3], [2, 4], [3, 1]]

# ----- 题15: 调试修复 - 找出以下代码中的 2 个 BUG [选做] -----
# 修复以下代码，使其能正确运行

# BUG: 语法 - 参数顺序错误，默认值参数不能在非默认值参数之前
def create_user( name,age=18):
    return {"name": name, "age": age}

# BUG: 逻辑 - 浅拷贝导致修改嵌套元素时影响原列表
import copy
original = [[1, 2], [3, 4]]
# backup = copy.copy(original)  # 应该用什么？
backup = copy.deepcopy(original)
backup[0][0] = 999
print(f"修改backup后 original = {original}")  # 不应该被修改
