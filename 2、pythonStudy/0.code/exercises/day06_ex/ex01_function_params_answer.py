"""
Day06 练习1 - 函数参数与参数传递（答案版）
"""

# ----- 题1: 必须参数与关键字参数 -----
def greet(name, msg):
    print(f"{name}, {msg}")

greet("Alice", "早上好")        # ✅ 答案: Alice, 早上好
greet(msg="下午好", name="Bob") # ✅ 答案: Bob, 下午好

print()

# ----- 题2: 参数默认值 -----
def power(base, exp=2):
    return base ** exp

print(power(3))     # ✅ 答案: 9
print(power(3, 3))  # ✅ 答案: 27
print(power(2, 5))  # ✅ 答案: 32

print()

# ----- 题3: 不定长参数 *args -----
def calc_sum(*args):
    print(f"args的类型: {type(args)}")
    print(f"args的值: {args}")
    return sum(args)

result = calc_sum(1, 2, 3, 4, 5)
print(f"求和结果: {result}")
# ✅ 答案:
# args的类型: <class 'tuple'>
# args的值: (1, 2, 3, 4, 5)
# 求和结果: 15

print()

# ----- 题4: 不定长参数 **kwargs -----
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=20, city="北京")
# ✅ 答案:
# name: 张三
# age: 20
# city: 北京

print()

# ----- 题5: 解包传参 -----
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
info = {"a": 10, "b": 20, "c": 30}

print(add(*nums))   # ✅ 答案: 6
print(add(**info))   # ✅ 答案: 60

print()

# ----- 题6: 参数传递 - 不可变对象 -----
def modify_int(x):
    print(f"函数内修改前: x={x}, id={id(x)}")
    x = 100
    print(f"函数内修改后: x={x}, id={id(x)}")

a = 10
print(f"函数调用前: a={a}, id={id(a)}")
modify_int(a)
print(f"函数调用后: a={a}, id={id(a)}")
# ✅ 答案:
# 函数调用前: a=10, id=xxx
# 函数内修改前: x=10, id=xxx（与a的id相同）
# 函数内修改后: x=100, id=yyy（新对象）
# 函数调用后: a=10, id=xxx（不受影响）

print()

# ----- 题7: 参数传递 - 可变对象 -----
def modify_list(lst):
    print(f"函数内修改前: {lst}, id={id(lst)}")
    lst.append(4)
    print(f"函数内修改后: {lst}, id={id(lst)}")

my_list = [1, 2, 3]
print(f"函数调用前: {my_list}, id={id(my_list)}")
modify_list(my_list)
print(f"函数调用后: {my_list}, id={id(my_list)}")
# ✅ 答案:
# 函数调用前: [1, 2, 3], id=xxx
# 函数内修改前: [1, 2, 3], id=xxx（相同）
# 函数内修改后: [1, 2, 3, 4], id=xxx（相同，原地修改）
# 函数调用后: [1, 2, 3, 4], id=xxx（被修改了！）

print()

# ----- 题8: 函数内重新赋值 vs 修改元素 -----
def try_replace(lst):
    lst = [99, 100, 101]
    print(f"函数内: {lst}")

def try_modify(lst):
    lst[0] = 99
    print(f"函数内: {lst}")

list1 = [1, 2, 3]
try_replace(list1)
print(f"try_replace后: {list1}")  # ✅ 答案: [1, 2, 3]（不受影响）

list2 = [1, 2, 3]
try_modify(list2)
print(f"try_modify后: {list2}")   # ✅ 答案: [99, 2, 3]（被修改）

print()

# ----- 题9: 带 * 的不定长参数的位置规则 -----
def func(a, *args, b):
    print(f"a={a}, args={args}, b={b}")

func(1, 2, 3, 4, b=5)
# ✅ 答案: a=1, args=(2, 3, 4), b=5

# 以下代码会报错吗？
# func(1, 2, 3, 4, 5)
# ✅ 答案: 会报错 TypeError，因为 *args 后面的 b 必须用关键字传参

print()

# ----- 题10: 浅拷贝与深拷贝 -----
import copy

original = [1, [2, 3], 4]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[1][0] = 99
deep[1][1] = 88

print(f"original = {original}")  # ✅ 答案: [1, [99, 3], 4]（浅拷贝修改影响了原对象）
print(f"shallow  = {shallow}")   # ✅ 答案: [1, [99, 3], 4]
print(f"deep     = {deep}")      # ✅ 答案: [1, [2, 88], 4]（深拷贝独立，不影响原对象）

print()

# ----- 题11: 浅拷贝的多种方式 -----
import copy

original = [[1, 2], [3, 4]]

c1 = original.copy()
c2 = original[:]
c3 = list(original)
c4 = copy.copy(original)

print(c1 is original)  # ✅ 答案: False（新对象）
print(c2 is original)  # ✅ 答案: False（新对象）

c1[0][0] = 999
print(f"original = {original}")  # ✅ 答案: [[999, 2], [3, 4]]（子对象共享）
print(f"c1 = {c1}")              # ✅ 答案: [[999, 2], [3, 4]]

print()

# ----- 题12: 参数传递的本质 -----
def mystery(lst):
    lst += [4, 5]  # += 对列表是原地修改（等价于 lst.extend([4, 5])）

data = [1, 2, 3]
mystery(data)
print(f"data = {data}")  # ✅ 答案: [1, 2, 3, 4, 5]（被修改了）

def mystery2(lst):
    lst = lst + [4, 5]  # = 是重新赋值，创建新对象

data2 = [1, 2, 3]
mystery2(data2)
print(f"data2 = {data2}")  # ✅ 答案: [1, 2, 3]（不受影响）

print()

# ----- 题13: 函数返回多个值的本质 -----
def get_info():
    return "张三", 20, "北京"

result = get_info()
print(f"result = {result}")       # ✅ 答案: ('张三', 20, '北京')
print(f"type = {type(result)}")   # ✅ 答案: <class 'tuple'>

name, age, city = get_info()
print(f"name={name}, age={age}, city={city}")  # ✅ 答案: name=张三, age=20, city=北京

print()

# ----- 题14: 综合应用 - 参考实现 -----
import copy

def safe_sort(nested_list):
    # 参考实现:
    temp = copy.deepcopy(nested_list)
    temp.sort(key=lambda x: x[0])
    return temp

test_data = [[3, 1], [2, 4], [1, 3]]
result = safe_sort(test_data)
print(f"原数据: {test_data}")    # 预期: [[3, 1], [2, 4], [1, 3]]（不变）
print(f"排序后: {result}")       # 预期: [[1, 3], [2, 4], [3, 1]]

print()

# ----- 题15: 调试修复 - 参考答案 -----
# BUG 修复1: 默认值参数必须放在非默认值参数之后
def create_user(name, age=18):  # 修复: 调换参数顺序
    return {"name": name, "age": age}

# BUG 修复2: 应该使用深拷贝而不是浅拷贝
import copy
original = [[1, 2], [3, 4]]
backup = copy.deepcopy(original)  # 修复: 使用 deepcopy
backup[0][0] = 999
print(f"修改backup后 original = {original}")  # 现在不会被修改了
