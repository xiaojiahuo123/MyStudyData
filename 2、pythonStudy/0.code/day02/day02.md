![](E:\Code\MyStudyData\2、pythonStudy\0.code\day02\images\1.png)

day02学习内容:

##### 1、进制基础

二进制表示用0b开头，例如 0b0001，八进制以0o开头，例如0o3，十六进制以0x表示，其中10到15用A B C D E F表示

二进制的计算方法，八进制的计算方法，十六进制的计算方法，三个进制的互相转换方法（进制转换函数），转换为二进制函数bin()  转换为八进制函数oct()  转换为十六进制函数hex()

原码、反码、补码，正数的三码一致，负数的原码是二进制的最左边为1，反码是0边1，1变0，补码是反码（二进制）加1

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