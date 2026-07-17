"""
    该案例演示了链表
"""

class Node:
    """定义链表中的节点类"""
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    """定义链表类"""
    def __init__(self):
        self.__head = None
        self.__size = 0


    def __str__(self):
        res = []
        node = self.__head
        while node:
            res.append(str(node.data))
            node = node.next
        return "->".join(res)

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0


    def insert(self, index, item):
        """向链表中指定的位置插入元素"""
        if index < 0 or index > self.__size:
            raise IndexError("链表越界")

        if index == 0:
            # 说明要向头节点的位置添加元素  这个新添加的元素下一个元素指向原来的头，整个链表的头变成当前节点
            self.__head = Node(item, self.__head)
        else:
            node = self.__head
            for i in range(index - 1):
                node = node.next

            # 创建新的节点封装要插入的数据   当前新节点指向原来上一个节点的下一个节点
            # 原来上一个节点的下一个节点 指向了当前节点
            node.next = Node(item,node.next)

        self.__size += 1

    def append(self, item):
        """向链表末尾追加元素"""
        self.insert(self.__size, item)


    def remove(self, index):
        """从列表中删除指定位置的元素"""
        if index < 0 or index >= self.__size:
            raise IndexError("链表越界")

        if index == 0:
            # 删除头结点
            self.__head = self.__head.next
        else:
            # 获取到要删除的节点的上一个节点
            node = self.__head
            for i in range(index-1):
                node = node.next
            node.next = node.next.next
        self.__size -= 1

    def set(self,index,item):
        """修改链表中指定位置的元素"""
        if index < 0 or index >= self.__size:
            raise IndexError("链表越界")

        node = self.__head
        for i in range(index):
            node = node.next
        node.data = item

    def get(self, index):
        """访问元素"""
        if index < 0 or index >= self.__size:
            raise IndexError
        node = self.__head
        for i in range(index):
            node = node.next
        return node.data

    def find(self, item):
        """判断当前链表中是否存在指定的元素"""
        node = self.__head
        while node:
            if node.data == item:
                return True
            node = node.next
        return False

    def for_each(self, func):
        node = self.__head
        while node:
            func(node.data)
            node = node.next

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.insert(0, 10)
llist.remove(0)
print(llist)
llist.set(0,10)
print(llist)
# print(llist.find(1))
# print(llist.get(2))
# llist.for_each(print)
