"""
    该案例演示了动态删除属性与方法
        del 对象.属性名
        delattr(对象，属性名)
"""
class Student:
    home = "atguigu"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat")


zs = Student("zs",20)
zs.eat()
delattr(zs,"eat") 
# delattr 只能删除对象自身的属性 ，不能删除从类继承的方法。
# 要删除类方法，需要对 类 操作而不是对 实例 操作
zs.eat()

