"""
    该案例演示了raise抛出异常
"""
def add(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x + y
    else:
        # 抛出异常
        pass
        raise TypeError("参数类型错误")


try:
    # 可能发生异常的代码
    print(add(1, 2.0))
except TypeError as e:
    # 对异常处理的代码
    print(e)
    # print("发生异常了")
except Exception as e:
    print(f"程序运行的时候发生了异常：{e}")

print("end")
# print(add(1, 2.0))