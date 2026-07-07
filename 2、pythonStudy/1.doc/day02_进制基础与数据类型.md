![](E:\Code\MyStudyData\2、pythonStudy\0.code\day02\images\1.png)

day02学习内容:

##### 1、进制基础

二进制表示用0b开头，例如 0b0001，八进制以0o开头，例如0o3，十六进制以0x表示，其中10到15用A B C D E F表示

二进制的计算方法，八进制的计算方法，十六进制的计算方法，三个进制的互相转换方法（进制转换函数），转换为二进制函数bin()  转换为八进制函数oct()  转换为十六进制函数hex()

原码、反码、补码，正数的三码一致，负数的原码是二进制的最左边为1，反码是0边1，1变0，补码是反码（二进制）加1

###### 二进制加法

```python
#公式：
a + b = (a ^ b) + ((a & b) << 1)
- a ^ b = 不考虑进位的加法结果
- (a & b) << 1 = 进位值（左移表示进位到高位）
- 两者相加就是最终结果
```

a + b = (a ^ b) + ((a & b) << 1)

##### 2、数据类型

数据类型，int float bool String 复数 ，type（）函数判断数据是什么类型， isinstance(num1, bool)  判断变量的类型，type() 不会认为子类是一种父类类型，isinstance() 会认为子类是一种父类类型。

小证整数池（-6，256）这个范围的数是直接用的内存里的小整数池的同一个对象

```python
print(id(num1)) # id(num1) 这个函数是获取变量在内存中的地址

# is 判断左右两边是否指向内存中的同一个地址
print(num1 is True)
print(num2 is False)
```

数据类型转换（自动转换和强制转换）

```python
# 自动类型转换
num1 = 1
num2 = 0.5
print(type(num1), type(num2)) #输出num1是int，num2是float

num1 = int("12",16)  # 转换为INT
num1 = float("5")  # 将x转换为一个浮点数
num1 = complex(2,3)  # 创建一个实部为real，虚部为imag的复数
print(str(str1))  # 将对象x转换为一个字符串
eval(2+3)	# 输出为5，此函数执行x字符串表达式，并返回表达式的值
chr(x)  # 将一个整数转换为一个Unicode字符
```

字符串的编码与解码

```python
"""
    该案例演示了字符的编码以及解码
        编码：将字符转换为字节的形式
        解码：将字节转换为字符的形式
"""
str1 = "你好中国"
print(str1)
print(type(str1))
# 编码
byte1 = str1.encode(encoding='gbk')  # 此处使用encode()函数将str1编码为了gbk格式的字节
print(byte1)
print(type(byte1))

# 解码
# str2 = byte1.decode(encoding='utf-8')
# print(str2)

# 注意：编码和解码需要指定相同的字符集
str3 = byte1.decode(encoding='gbk')  # 此处将字节byte1解码为字符串
print(str3)
```

输入和输出，以及输出的格式化使用format

其中format()已经在day01文档中解释

bool是int的子类

![](.\images\2.png)

对于int()函数，

```python
# Python 伪代码演示 int() 的工作原理
def my_int(s: str, base: int) -> int:
    result = 0
    for char in s:
        # 将字符转换为对应的数字
        if char.isdigit():
            digit = int(char)
        else:
            digit = 10 + ord(char.lower()) - ord('a')
        
        # 核心算法
        result = result * base + digit
    
    return result

# 测试
print(my_int("12", 16))   # 18
print(my_int("1A", 16))   # 26
print(my_int("1010", 2))  # 10
```

python中的int没有长度的限制，不会溢出

```python
# 整数相加时的扩展逻辑
PyObject *
PyLong_Add(PyObject *v, PyObject *w)
{
    PyLongObject *a, *b, *result;
    Py_ssize_t size_a, size_b, size;
    
    # 获取两个数的位数
    size_a = Py_SIZE(a);
    size_b = Py_SIZE(b);
    
    # 计算结果需要的位数
    size = Py_MAX(size_a, size_b) + 1;  # +1 用于进位
    
    # 分配新的数组空间
    result = _PyLong_New(size);
    
    # 执行加法运算...
}

C语言 int 有限制的原因 ：

- 使用固定大小的内存（通常4字节）

- 受硬件和操作系统限制

- 超过范围会发生溢出（未定义行为）

Python int 无限制的原因 ：

- 使用 可变长度数组 存储

- 位数不够时自动扩展

- 只受可用内存限制

- 理论上可以表示任意大的整数C语言 int 有限制的原因 ：
```