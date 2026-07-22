class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self):
        self.__size = 0  # 哈希表的元素的个数
        self.__capacity = 2  # 容量
        self.__table = [None] * self.__capacity  # 存储哈希表的元素的列表
        self.____load_factor = 0.7  # 负载因子

    def __hash(self,key):
        index = hash(key) % self.__capacity
        return index

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def display(self):
        # super.__str__(self)
        for i,node in enumerate(self.__table):
            print(f"索引为{i}",end=' ')
            current = node
            while current:
                print(f"({current.key},{current.value})",end='->')
                current = current.next
            print("None")

    def __grow(self):
        self.__capacity *= 2
        # old_table = self.__table
        self.__table,old_table = [None] * self.__capacity,self.__table  # 解包写法
        self.__size = 0
        for i,node in enumerate(old_table):
            # self.__table[i] = node  # 不能直接这样添加，因为涉及到哈希冲突的时候需要链表
            pass

    def put(self,key,value):
        if self.__size / self.__capacity > self.____load_factor:
            # 超过负载因子触发扩容
            self.__grow()
        index = self.__hash(key)
        if self.__table[index] is None:  # index处无节点
            self.__table[index] = Node(key,value)
        else:
            current = self.__table[index]
            while current:
                if current.key == key:  # 实际上是修改，原本存储的key就是现在需要添加的
                    current.value = value
                    return
                if not current.next:
                    # current = current.next
                    break  # 直接用这里结束循环，而不需要等到while的循环条件为False
                current = current.next
            current.next = Node(key, value)
        self.__size += 1

    def remove(self,key):
        # 这是我原本对于remove的实现
        # index = hash(key) % self.__capacity
        # if self.__table[index] is None:
        #     # raise KeyError('Key not found')
        #     return False
        # del(self.__table[index])
        # return True

        index = self.__hash(key)
        current = self.__table[index]
        # 代表上一个节点
        prev = None  # 初始化prev为None

        while current:
            if current.key == key:  # 这里之所以在上面根据key计算处index获取节点元素后，还要判断current.key == key，
                # 是因为哈希表中的哈希冲突，可能计算的key是这个index,但是index处的节点的key不是这个key
                if prev:
                    # 说明删除的不是头节点
                    prev.next = current.next  # 这是直接上一个节点的next指向下一个节点，越过了现在的这个节点实现删除
                else:
                    # 说明删除的是头节点
                    self.__table[index] = current.next  # 直接用下一个节点放到头节点，实现对于原本的头节点的删除
                self.__size -= 1
                return True
            prev = current  # 更新prev为当前节点
            current = current.next  # 更新current为下一个节点，继续遍历
        return False

    def get(self, key):
        index = hash(key)
        if self.__table[index] is None:
            return None
        return self.__table[index]

    def for_each(self,func):
        if self.__table is None:
            return  None
        for i,node in enumerate(self.__table):
            func(node)
        return None


hs = MyHashTable()
hs.put(1,10)
hs.put(2,20)
hs.put(3,30)
hs.put(1,80)
# hs.remove(3)
# print(hs.get(3))
hs.display()
# print(hs.__str__())
# hs.for_each(print)

