"""
Day02 练习2 - 输入输出与格式化
由浅入深掌握 Python 的输入输出

参考源码: Objects/unicodeobject.c (字符串格式化底层)
         Lib/_pyio.py (IO模块)
"""
from tokenize import String

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 基本输入输出 -----
# 从键盘输入用户名和年龄，格式化输出
# 示例: "你好，小明！你今年18岁。"
# TODO:
# print(f"你好,{input()}!你今年{input()}岁！") 不太好没格式限制
# name : String  = input()
# age : int = int(input())
# print(f"你好，{name},你今年{age}岁!")
# 获取用户输入（带提示信息）
name = input("请输入你的姓名：")

# 获取年龄并处理可能的错误
while True:
    try:
        age = int(input("请输入你的年龄："))
        if age < 0 or age > 150:
            print("请输入有效的年龄（0-150）")
            continue
        break
    except ValueError:
        print("请输入有效的数字作为年龄")

# 格式化输出（注意中文标点和格式）
print(f"你好，{name}！你今年{age}岁。")

# ----- 题2: % 格式化 (旧式风格) -----
price = 9.5
quantity = 7
total = price * quantity
# TODO: 用 % 格式化输出: "单价: 9.50元, 数量: 7, 总价: 66.50元"
# %d=整数, %f=浮点数, %s=字符串, %%=百分号
print("单价: %.2f元, 数量: %d, 总价: %.2f元" % (price, quantity, total))

# ----- 题3: format() 方法 -----
pi = 3.14159265
# TODO: 用 format 输出保留4位小数: "圆周率为 3.1416"
print("圆周率为{:.4f}".format(pi))
print(f"圆周率为{pi:.4f}")
# TODO: 用 format 居中对齐，总宽度20，用*填充


# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题4: format 格式规范 -----
num = 1234567.89
# 用 format 实现以下格式:
# 千分位分隔:     1,234,567.89
# 百分比:         0.856 -> 85.60%
# 科学计数法:     1234567.89 -> 1.23e+06
# 二进制:         42 -> 101010
# 十六进制大写:   255 -> FF
# TODO:
print("千分位分隔: {:,}".format(num))
percent = 0.856
print("百分比: {:.2%}".format(percent))
# 科学计数法
print("科学计数法: {:.2e}".format(num))
print("42转换为二进制{:b}".format(42))
# 十六进制大写
print("十六进制大写: {:X}".format(255))

# ----- 题5: f-string 高级用法 -----
name = "小明"
age = 18
score = 95.678

# TODO: 用 f-string 实现以下输出:
# (1) 调试语法: name='小明', age=18  (Python 3.8+ 用 {name=} 语法)
print(f"{name=}, {age=}, {score=}")
# (2) 对齐输出:
# 姓名          年龄          分数
# 小明          18            95.68
print("\n对齐输出:")
print(f"{'姓名':<12}{'年龄':<12}{'分数'}")
print(f"{name:<12}{age:<12}{score:.2f}")
# (3) 表达式: f"{age >= 18 and '成年' or '未成年'}"
print(f"\n年龄判断: {age >= 18 and '成年' or '未成年'}")
# (4) 格式化数字:
# 千分位: {num:,.2f}
# 填充对齐: {name:*^10}
print(f"千分位: {num:,.2f}")
print(f"填充对齐: {name:*^10}")

# ----- 题6: print() 的高级参数 -----
# end 参数: 控制结尾字符
# sep 参数: 控制分隔符
# flush 参数: 是否立即刷新缓冲区

# TODO: 用 print 打印一个简易进度条
# 提示: \r 回到行首, end="" 不换行
import time
# TODO: 实现 0% 到 100% 的进度条效果
import time

for i in range(1, 101):
    print(f"\r[{'=' * i:<100}] {i}%", end="")
    time.sleep(0.05)
print()  # 最后换行

# ----- 题7: 多行输入 -----
# input() 每次只能读一行，如何读取多行输入？
# 提示: 用循环 + 结束标记
# TODO: 实现一个简单的多行输入程序
# 输入 "quit" 结束，最后打印所有输入的内容


# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题8: 格式化的底层原理 -----
# f-string 在编译时被转换为 .format() 调用
# 可以用 dis 模块查看字节码
import dis

def test_fstring():
    name = "world"
    return f"hello {name}"

def test_format():
    name = "world"
    return "hello {}".format(name)

print("f-string 字节码:")
dis.dis(test_fstring)
print("\nformat() 字节码:")
dis.dis(test_format)
# 观察两者的字节码有什么不同？
# f-string 性能更好，因为编译时就确定了格式


# ----- 题9: input() 的本质 -----
# input() 读取的是字符串，需要手动转换类型
# 以下代码有什么问题？
# age = input("请输入年龄: ")
# print(age + 1)  # 会报错！

# TODO: 写一个健壮的输入程序
# 要求: 输入一个整数，如果输入不合法则提示重新输入
# 提示: try...except 处理异常

while True:
    try:
        age = int(input("请输入一个整数: "))
        break
    except ValueError:
        print("请输入有效的整数")



# ----- 题10: 字符串是不可变的 -----
# 所有字符串方法都返回新字符串，不修改原字符串
s = "Hello World"
print(f"原字符串: {s}, id={id(s)}")
s2 = s.lower()
print(f"lower(): {s2}, id={id(s2)}")
print(f"原字符串不变: {s}, id={id(s)}")
# 思考: 如果字符串很大，频繁修改会有什么性能问题？
# 如何高效拼接大量字符串？(提示: join)
