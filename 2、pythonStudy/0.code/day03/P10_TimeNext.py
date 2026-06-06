# 时间下一秒计算程序

print("=" * 40)
print("      计算下一秒的时间")
print("=" * 40)

# 从键盘输入时间（格式：HH:MM:SS）
time_str = input("请输入时间（格式：HH:MM:SS）：")

# 分割时间字符串，获取时、分、秒
time_parts = time_str.split(":")
hour = int(time_parts[0])
minute = int(time_parts[1])
second = int(time_parts[2])

# 计算下一秒
second += 1

# 处理秒数溢出（60秒进位到分钟）
if second == 60:
    second = 0
    minute += 1

# 处理分钟溢出（60分钟进位到小时）
if minute == 60:
    minute = 0
    hour += 1

# 处理小时溢出（24小时归零）
if hour == 24:
    hour = 0

# 输出结果（保持两位数格式）
print("-" * 40)
print(f"当前时间：{time_str}")
print(f"下一秒时间：{hour:02d}:{minute:02d}:{second:02d}")
print("-" * 40)
