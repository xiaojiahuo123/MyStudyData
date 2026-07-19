
class Myarray:
    def __init__(self):
        # self.__capacity = 0  # 数组容量,初始不能为0，否则扩容乘以2还是0
        self.__capacity = 8
        self.__size = 0  # 数组长度
        # self.__items = [0] * self.__size # 存储数组的列表 # 这里是存储数组的列表，不应该用self.__size，这是数组的长度，而应该使用self.__capacity
        self.__items = [0] * self.__capacity

    def __str__(self):  # 和 __init__一样的魔术方法，在- `print(obj)` 和 `str(obj)` 时**自动调用**，不需要手动调用
        res = "["
        for i in range(self.__size):
            res += str(self.__items[i])
            # res += " "  # 直接这样存在一个问题，那就是数组的最后一个元素的右边存在空格
            if i != self.__size - 1:
                res += ", "
        res += "]"
        return res

    @property  # 将方法转换为属性
    def size(self):
        """获取数组的元素个数"""
        return self.__size

    def is_empty(self):
        """判断数组是否为空"""
        return self.__size == 0  # 直接这样更加简洁，如果为空返回True否则返回false
        # if self.__size == 0:
        #     return True
        # return -1

    def __grow(self):
        """数组扩容"""
        # 先增加容量，再将旧数组放入新数组
        if self.__size == self.__capacity:
            self.__capacity *= 2
        new_items = [0] * self.__capacity
        for i in range(self.__size):
            new_items[i] = self.__items[i]

        self.__items = new_items


    def insert(self, index, value):
        """向数组中指定位置插入元素"""
        if index < 0 or index >= self.__size:  # 防止索引越界
            raise IndexError("index out of range")

        # self.__size += 1  # 这里应该放在最后执行，因为放在前面，等于在数组中原本的元素右移之前，就改变了长度，那么在右移的过程中就会出问题
        # 因为self.__items是按照容量创建的存储数组的列表，他的结构是这样的 : [1,2,3,... ,0 ,0,0,0]，后面的0是占位的，不是数组的元素，所以在整个类的方法中不使用 len(self.__items)
        # 因为这是数组的容量的长度，而不是数组的长度，因此必须使用self.__size
        # 也因此，下面在元素右移的时候，最右边的元素最极限的情况是占据原本self.__items最后一位占位的0，而不会被挤的没有位置
        if self.__size >= self.__capacity:
            self.__grow()
        # if self.__size >= self.__capacity:  # 数组扩容应该是一个独立的方法，因为还涉及将原本的数组放入扩容后的数组中
        #     self.__capacity *= 2

        # for i in range(index,self.__size -1):  # 不能这样正向的遍历，这样会让后一个元素直接被前一个元素覆盖，最终插入位置右边都变成了一个元素
        #     self.__items[i + 1] = self.__items[i]
        for i in range(self.__size - 1, index, -1):
            self.__items[i] = self.__items[i-1]

        self.__items[index] = value
        self.__size += 1

    def append(self, value):
        if self.__size >= self.__capacity:
            self.__grow()
            # 原本的函数，只是在容量不足的时候进行扩容，但是扩容后没有将追加的元素添加进去！
            self.__items[self.__size] = value
        else:
            self.__items[self.__size] = value
        self.__size += 1

    def remove(self, index):
        if index < 0 or index >= self.__size: raise IndexError("index out of range")
        for i in range(index,self.__size-1):
            self.__items[i] = self.__items[i+1]  # 元素左移
        self.__size -= 1  # 这里长度减少之后，原本的最后一个元素因为长度的变化成为了垃圾，python的垃圾回收会自动清理

    def set(self,index,value):
        if index < 0 or index >= self.__size: raise IndexError("index out of range")
        self.__items[index] = value

    def get(self,index):
        if index < 0 or index >= self.__size: raise IndexError("index out of range")
        return self.__items[index]

    def find(self,value):
        if self.__size == 0: return -1
        for i in range(self.__size):
            if self.__items[i] == value:
                return i
        return -1

    def for_each(self,fn):
        for i in range(self.__size):
            fn(self.__items[i])


arr1 = Myarray()
arr1.append(1)
arr1.append(2)
arr1.append(3)
arr1.append(4)
arr1.append(5)
arr1.append(6)
arr1.append(7)
arr1.append(8)
# arr1.insert(0,5)
print(arr1)
# arr1.for_each(print)
arr1.remove(2)
print(arr1)