"""
    该案例演示了栈数据结构
"""
class Stack:
    def __init__(self):
        # 用动态数组(python中的列表) 存储栈中元素
        self.__items = []
        # 栈中元素的个数
        self.__size = 0

    @property
    def size(self):
        """返回栈中元素个数"""
        return self.__size

    def is_empty(self):
        """判断栈是否为空"""
        return self.__size == 0

    def push(self, item):
        """入栈|压栈|进栈:将元素放到栈中"""
        self.__items.append(item)
        self.__size += 1

    def pop(self):
        """出栈|弹栈 :从栈中将元素删除掉"""
        # 判断栈中元素是否为空
        if self.is_empty():
            raise Exception("栈为空")

        item = self.__items[self.__size - 1]
        del self.__items[self.__size - 1]

        self.__size -= 1
        return item

    def peek(self):
        """获取栈顶元素，但是不出栈"""
        if self.is_empty():
            raise Exception("栈为空")
        return self.__items[self.__size - 1]

mys = Stack()
mys.push(1)
mys.push(2)
mys.push(3)
print(mys.size)
# print(mys.pop())
print(mys.peek())
print(mys.size)
