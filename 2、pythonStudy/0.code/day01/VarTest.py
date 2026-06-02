var1 = 2
var2 = 3
result = var1 + var2
print(result)
name = "John"
age = 22
weight = 1000.0
print(f"{name} {age} {weight}")
# Python 不需要用分号结尾，虽然语法上允许，但不符合 Python 风格
# print(f"{name} {age} {weight}") 使用了 Python f-string （格式化字符串字面量），
# 这是 Python 3.6+ 引入的一种优雅的字符串格式化方式。

var1 = 2
var2 = 20
print(var1, var2) # 2 20

var1, var2 = var2, var1
print(var1, var2) # 20 2

# 十进制
dec = 10
# 二进制 以0b开头
binary_number = 0b1010
# 八进制 以0o开头
octal_number = 0o12
# 十六进制 以0x开头
hex_number = 0xA

print(f"十进制:{dec} 二进制{binary_number} 八进制 {octal_number} 十六进制 {hex_number}")
