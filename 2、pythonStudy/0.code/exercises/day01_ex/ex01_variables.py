"""
Day01 练习1 - 变量与f-string
由浅入深，掌握变量本质和字符串格式化

参考源码: Objects/longobject.c (整数对象)
         Objects/unicodeobject.c (字符串对象)
"""
from secrets import token_hex

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 变量赋值与输出 -----
# 定义姓名、年龄、身高(米)三个变量，用 f-string 输出
# 期望: "我叫小明，今年18岁，身高1.75米"
print("----- 题1: 变量赋值与输出 -----")
name = "小明"
age = 18
height = 1.75
# TODO: 用 f-string 输出
print(f"我叫{name}，今年{age}岁，身高{height}米 ")


# ----- 题2: 变量交换 -----
# 不使用第三个变量，交换 a 和 b 的值
print("----- 题2: 变量交换 -----")
a = 10
b = 20
# TODO: 写你的代码
a,b = b,a
print(f"交换后 a={a}, b={b}")  # 期望: a=20, b=10

# ----- 题3: 多变量赋值 -----
# 用一行代码同时给 x, y, z 赋值为 100, 200, 300
# 再用一行交换 x 和 z
# TODO:
print("----- 题3: 多变量赋值 -----")
x,y,z = 100,200,300
x,z = z,x
print(f"x={x}, y={y}, z={z}")  # 期望: x=300, y=200, z=100


# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题4: 进制转换 -----
# 将十进制数 255 分别转换为二进制、八进制、十六进制
# 再将二进制 0b11111111 转回十进制验证
num = 255
# TODO:
# num = bin(num)  # num = "0b11111111"（字符串）
# print(f"二进制：{num}")
# num = oct(num)  # ❌ 错误！oct() 只能用于整数，不能用于字符串
# print(f"八进制：{num}")
print(f"二进制：{num:08b}")
print(f"八进制：{num:03o}")
print(f"十六进制：{num:02x}")

# ----- 题5: f-string 对齐与填充 -----
# 用 f-string 实现以下输出效果:
# **********成绩表**********
# * 姓名      分数         *
# * 小明      95           *
# * 小红      88           *
# * 小刚      72           *
# ****************************
# 提示: f-string 支持 {value:<10} 左对齐, {:>10} 右对齐, {:^10} 居中
# TODO:
print(f"\n{'*' * 10}成绩表{'*' * 10}")
print(f"* {'姓名':<10} {'分数':<10}*")
print(f"* {'小明':<10} {95:<10} *")
print(f"* {'小红':<10} {88:<10} *")
print(f"* {'小刚':<10} {72:<10} *")
print(f"{'*' * 28}")

# ----- 题6: f-string 表达式 -----
# f-string 中可以直接写表达式，输出以下结果:
# "3 + 5 = 8"
# "10 / 3 = 3.33"
# "大写: HELLO"
# TODO:


# ----- 题7: 多重赋值的本质 -----
# 预测以下代码的输出，然后运行验证
a = [1, 2, 3]
b = a           # b 和 a 指向同一个列表对象
b.append(4)
print(f"a = {a}")   # 预测: ____1,2,3,4
print(f"b = {b}")   # 预测: ____1,2,3,4
print(f"a is b: {a is b}")  # 预测: ____TRUE

# 解释为什么 a 也变成了 [1, 2, 3, 4]？
# 提示: Python 的变量是"标签"而不是"盒子"
# 参考源码: Objects/listobject.c 中 PyListObject 的定义
#           列表对象在堆上分配，变量名只是对它的引用
# typedef struct { 这是python中list的c源码，
#     Py_ssize_t allocated; 已分配的元素数量
#     PyObject *ob_item[]; 指向堆上分配的元素数组的指针
# } _PyListArray;
# // 简化的伪代码
# PyObject *list_a = PyList_New(3);  // 在堆上创建
# PyObject *list_b = list_a;          // 只是指针赋值
# Py_INCREF(list_b);                  // 增加引用计数

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题8: 小整数池 -----
# Python 会缓存 [-5, 256] 范围内的整数对象
# 预测以下代码的输出
a = 256
b = 256
print(f"a is b (256): {a is b}")   # 预测: ____TRUE

a = 257
b = 257
print(f"a is b (257): {a is b}")   # 预测: ___TRUE_ (在同一行赋值时CPython可能优化)
# print(f"a is b (257): {a is b}")输出为TRUE，这是 另一个机制 ： CPython 编译器的常量去重优化 ， 不是小整数池
# 为什么 256 和 257 的行为不同？
# 参考源码: Objects/longobject.c 中的 small_ints 数组
# Python 启动时预创建了 -5 到 256 的整数对象


# ----- 题9: 字符串驻留 (Interning) -----
# Python 会对某些字符串进行驻留(缓存复用)
a = "hello"
b = "hello"
print(f"'hello' is 'hello': {a is b}")  # 预测: ____true

a = "hello world!"
b = "hello world!"
print(f"'hello world!' is 'hello world!': {a is b}")  # 预测: ____true

a = "".join(["h", "e", "l", "l", "o"])
b = "hello"
print(f"join结果 is 'hello': {a is b}")  # 预测: ____

# 思考: 哪些字符串会被驻留？为什么 Python 要这样做？
# 参考源码: Objects/unicodeobject.c 中的 PyUnicode_InternInPlace
""""
- 编译期优化 ：Python 编译器在解析源代码时，会创建一个 常量池 存储所有字符串字面量
- 常量去重 ：相同内容的字符串字面量只存储一次，后续使用时复用同一个对象
- 字节码生成 ：生成的字节码使用 LOAD_CONST index 指令加载常量，相同字符串共享同一个索引
"""

# ----- 题10: id() 与内存地址 -----
# id() 返回对象的内存地址（CPython中就是内存地址）
a = 100  # a 是指向小整数池的指针
b = 100
c = a  #不创建新对象 ，只是复制指针,修改 c 不会影响 a（因为整数是不可变的）,如果 c = 200,只是c 现在指向另一个对象，a 仍然指向 100
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")
print(f"id(a) == id(b): {id(a) == id(b)}")
print(f"id(a) == id(c): {id(a) == id(c)}")

# 思考: 为什么 c = a 之后，id(c) 和 id(a) 相同？
# 这说明 Python 赋值操作的本质是什么？  id()是获取变量的内存地址，a is b 是判断 a 和 b 是否指向同一个对象
"""
这里，我认为是100属于小整数池的范围，所以a、b、c三个变量指向的是堆上的同一个地址，所以用id(）方法三者相同
"""

# ----- 题11: 可变对象 vs 不可变对象 -----
# 整数、字符串是不可变对象，列表是可变对象
s = "hello"
print(f"修改前 id(s) = {id(s)}")
s = s + " world"
print(f"修改后 id(s) = {id(s)}")
# 思考: id 变了吗？为什么？

lst = [1, 2, 3]
print(f"修改前 id(lst) = {id(lst)}")
lst.append(4)
print(f"修改后 id(lst) = {id(lst)}")
# 思考: id 变了吗？为什么列表和字符串的行为不同？
# 参考源码: Objects/listobject.c 中 listappend 函数
#           列表在原地修改，不创建新对象


# ----- 题12: 变量命名规则 -----
# 以下哪些变量名是合法的？先预测，再运行验证
# valid_name = 1      # 预测: ____TRUE
# 2name = 1           # 预测: ____FLASE
# _private = 1        # 预测: ____TRUE
# my-name = 1         # 预测: ____flase,-减号不能用
# class = 1           # 预测: ____flase,class是python关键字
# myName = 1          # 预测: ____TRUE
# __init__ = 1        # 预测: ____TRUE
# name@ = 1           # 预测: ____FALSE,@是非法的
# 变量命名规则总结：
# - 只能包含字母、数字、下划线
# - 不能以数字开头
# - 不能是Python关键字