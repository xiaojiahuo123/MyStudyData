"""
    该案例演示了hashtable
"""
class Node:
    """定义链表上的节点类"""
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        # 哈希表表中元素的个数
        self.__size = 0
        # 哈希表数组的容量
        self.__capacity = 2
        # 哈希表表中数组部分
        self.__table = [None] * self.__capacity
        # 负载因子（元素个数/数组容量）
        self.__load_factor = 0.7

    def __hash(self,key):
        return hash(key) % self.__capacity

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def display(self):  # 哈希表特有的 ，用来可视化输出哈希表内部结构的方法。
        for i,node in enumerate(self.__table):
            print(f"索引为{i}:",end="")
            current = node
            while current:
                print(f"({current.key},{current.value})->",end="")
                current = current.next
            print("None")


    def __grow(self):
        """扩容数组"""
        self.__capacity *= 2
        self.__table,old_table = [None] * self.__capacity,self.__table
        self.__size = 0

        for node in old_table:
            current = node
            while current:
                self.put(current.key,current.value)  
                # 这里哈希表实现存储键值对节点的列表self.__table，所以利用put方法，将旧数组中的元素插入到新的数组中
                current = current.next



    def put(self,key,value):
        """向hash表中添加元素"""
        # 如果元素个数/数组容量> 负载因子 ，需要扩容
        if self.__size/self.__capacity > self.__load_factor:
            self.__grow()

        # 计算当前kv要操作的数组元素下标
        index = self.__hash(key)
        # 封装节点对象
        new_node = Node(key,value)

        # 如果数组下标位置还没有元素，直接将当前元素作为头节点
        if self.__table[index] is None:
            self.__table[index] = new_node
        else:
            # 数组下标位置已经有元素
            current = self.__table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    # 没有走上面的 if，说明现在的key不在哈希表中，外层的判断else代表这里的key计算的index是存在的
                    # 这就说明，是不同的key经过哈希函数计算后指向了相同的index，发生了哈希冲突，需要将新的节点和index原本位置的节点组成链表
                    break
                current = current.next

            current.next = new_node
        self.__size += 1

    def remove(self,key):
        """根据key删除哈希表中元素"""
        # 获取数组对应的下标
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

    def get(self,key):
        """根据key获取对应的value"""
        index = self.__hash(key)
        current = self.__table[index]
        while current:
            if current.key == key:
               return current.value
            current = current.next
        return None

    def for_each(self,func):
        """遍历哈希表中的所有元素"""
        for node in self.__table:
            current = node
            while current:
                func(current.key,current.value)
                current = current.next


hs = HashTable()
hs.put(1,10)
hs.put(2,20)
hs.put(3,30)
hs.put(1,80)
# hs.remove(3)
# print(hs.get(3))
hs.display()
# hs.for_each(print)
