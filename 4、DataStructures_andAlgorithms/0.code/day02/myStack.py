class myStack:
    def __init__(self):
        self.__list = []
        self.__size = 0

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def push(self,item):
        """元素进栈"""
        self.__list.append(item)
        self.__size += 1

    def pop(self):
        """弹出栈顶元素"""
        if self.is_empty():
            raise IndexError("栈内元素为空！")
        item = self.__list[self.__size - 1]
        del self.__list[self.__size - 1]
        # self.__list[self.__size - 1] = None # 直接将栈顶元素赋值未None，但是实际上列表还是存在这个元素的，至于self.__size，这是我为了实现做的栈的元素的数量，而不是列表的长度
        self.__size -= 1
        return item

    def peek(self):
        """获取栈顶元素，但是不出栈"""
        if self.is_empty():
            raise   IndexError("栈内元素为空！")
        return self.__list[self.__size - 1]


mys = myStack()
mys.push(1)
mys.push(2)
mys.push(3)
print(mys.size)
# print(mys.pop())
print(mys.peek())
print(mys.size)