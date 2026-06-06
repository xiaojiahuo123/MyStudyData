# 用户登录验证程序

print("=" * 30)
print("      用户登录系统")
print("=" * 30)

# 获取用户名输入
username = input("请输入用户名：")

# 获取密码输入（使用input但不在终端显示密码）
password = input("请输入密码：")

# 验证登录信息
if username == "admin" and password == "123":
    print("-" * 30)
    print("登录成功！")
    print("-" * 30)
else:
    print("-" * 30)
    print("登录失败！用户名或密码错误。")
    print("-" * 30)
