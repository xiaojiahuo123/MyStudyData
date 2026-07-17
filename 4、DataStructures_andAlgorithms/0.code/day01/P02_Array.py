
    # 该案例演示了Python中的数组
    # 注意：python的内建中没有提供数组类型
    # 但是在python的array模块中提供了数组，另外在后续要用到的numpy模块中也提供了数组
    # 数组数据结构特点：
    #     线性的
    #     连续存储的，在内存中分配一片连续的存储空间
    #     只能存储相同数据类型的元素
    #     数组中的每一个元素都有下标，下标从0开始，可以通过下标访问数组元素
    #     数组容量一旦确定，就不能改变，如果需要扩容，需要通过额外的方法实现

import array
arr1 = array.array('i', [1, 2, 3])
print(id(arr1[0]))
num = 1
print(id(num))

# size()	返回数组中元素个数
# is_empty()	判断数组是否为空
# insert(index, item)	在指定位置插入元素
# append(item)	在末尾插入元素
# remove(index)	删除指定位置的元素
# set(index, item)	修改指定位置的元素
# get(index)	获取指定位置的元素
# find(item)	查找数组中某个元素的位置
# for_each(func)	遍历数组

class MyArray:
    def __init__(self):
        # 数组的容量
        self.__capacity = 8
        # 数组中元素的个数
        self.__size = 0
        # 数组底层用于存储数据的list
        self.__items = [0] * self.__capacity

    def __str__(self):
        res = "["
        for i in range(self.__size):
            res += str(self.__items[i])
            if i != self.__size - 1:
                res += ", "
        res+= "]"
        return res

    @property
    def size(self):
        """获取数组中元素的个数"""
        return self.__size

    def is_empty(self):
        """判断数组是否为空"""
        return self.__size == 0

    def __grow(self):
        """对数组容量进行扩容"""
        self.__capacity *=  2
        # 创建新的数组  容量是老数组的2倍
        new_items = [0] * self.__capacity
        # 将老数组中的元素搬到新数组
        for i in range(self.__size):
            new_items[i] = self.__items[i]

        # 将存储元素的地址 指向新的列表
        self.__items = new_items

    def insert(self, index,item):
        """向数组中插入元素"""
        # 判断下标是否越界
        if index < 0 or index > self.__size:
            raise IndexError("index out of range")

        # 判断数组容量是否够用
        if self.__size == self.__capacity:
            # 如果数组中元素的个数 和容量相等  需要进行扩容
            self.__grow()

        # 从右向左进行遍历，进行后移操作
        # 之所以这里右移，是因为这是插入方法，需要将数组中元素向后移动，才能插入新的元素
        for i in range(self.__size,index,-1):
            # range(start,stop,step)
            # start: 开始值  可以省略  默认是0
            # stop: 结束值  可以省略  默认是0
            # step: 步长  可以省略  默认是1
            self.__items[i] = self.__items[i-1]

        self.__items[index] = item
        self.__size += 1

    def append(self, item):
        """向数组中追加元素"""
        self.insert(self.__size,item)

    def remove(self, index):
        """到数组中删除指定位置的元素"""
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        for i in range(index,self.__size - 1) :
            self.__items[i] = self.__items[i+1]

        self.__size -= 1

    def set(self,index,item):
        """修改数组中指定位置的元素"""
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        self.__items[index] = item

    def get(self,index):
        """根据索引获取数组中指定位置的元素"""
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")
        return self.__items[index]

    def find(self,item):
        """查找元素在数组中第一次出现的位置下标"""
        for i in range(0,self.__size):
            if item == self.__items[i]:
                return i
        return -1

    def for_each(self,func):
        """遍历数组中元素"""
        for i in range(self.__size):
            func(self.__items[i])

arr1 = MyArray()
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






