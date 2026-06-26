"""
    该案例演示了封装
"""
class Person:
    __home = "earth"  # 实际存储为 _Person__home，这里是将他私有化了
    _test = "这是测试的，不是强制的私有化可以访问"

    def __init__(self, name, age):
        # __ 表示私有属性，只能在类内部访问
        # __ 表示私有方法，只能在类内部访问
        self.__name = name  # 实际存储为 self._Person__name
        self.age = age

    def __eat(self):
        print("eating")

    def eat_1(self):
        print("eating")
        print(self.__home)
        self.__eat()


print(Person._Person__home)

zs = Person("zs",18)
print(f"zs._test的值:{zs._test}")
print(zs._Person__name)
