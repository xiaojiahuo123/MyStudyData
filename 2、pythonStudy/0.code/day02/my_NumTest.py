# 二进制
b1 = 0b1010
# 十进制
b2 = 10
# 八进制
b3 = 0o12
# 十六进制
b4 = 0xA
print(f"{b1} {b2} {b3} {b4}")  # 这里输出会自动转换为10进制
print("~~~~~~~~")
print(f"{b1} 十进制为：{b1}")
print(f"{b2} 二进制为：{bin(b2)}")
print(f"{b3} 八进制为：{oct(b3)}")
print(f"{b4} 十六进制为：{hex(b4)}")
