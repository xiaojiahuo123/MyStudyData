"""
    该案例演示了自定义异常
"""
class MyException(Exception):
    def __init__(self, value):
        self.value = value


try:
    # 可能发生异常的代码
    # 第1步：进入try块
    # 第2步：执行 raise MyException(...)  → 主动抛出异常
    # 第3步：try块剩余代码跳过，跳到except
    # 第4步：匹配到 MyException，执行except块
    raise MyException("这是我自己定义的异常")
except MyException as e:
    # 对异常处理的代码
    print(f"发生异常了{e}")