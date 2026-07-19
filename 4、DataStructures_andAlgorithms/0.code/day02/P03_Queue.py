"""
    该案例演示了通过链表实现单向队列
"""
class Node:
    def __init__(self, data):
        # 当前节点存储的元素
        self.data = data
        # 下一个节点的引用
        self.next = None

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def size(self):
        """获取当前队列中元素的个数"""
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, data):
        """入队  向队列中添加元素 """
        new_node = Node(data)
        if self.is_empty():
            # 如果队列为空，说明当前添加的是队列中的第一个元素，将head和tail指向该节点
            self.__head = new_node
            self.__tail = new_node
        else:
            # 如果添加的不是队列中的第一个元素
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1


    def dequeue(self):
        """出队  从队列中取元素"""
        # 判断队列中是否有元素
        if self.is_empty():
            raise Exception("队列为空")

        # 取出队首元素的值
        data = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return data

    def peek(self):
        """访问队首元素"""
        if self.is_empty():
            raise Exception("队列为空")
        return self.__head.data

qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
print(qu.size)
# print(qu.dequeue())
print(qu.peek())
print(qu.size)




