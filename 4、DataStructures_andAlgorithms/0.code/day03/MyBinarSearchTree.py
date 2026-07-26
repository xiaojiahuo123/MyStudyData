from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class   MyBinarySearchTree:
    def __init__(self):
        self.__root = None  # 定义根节点
        self.__size = 0  # 树的节点数量

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def print_tree(self):
        """打印树的结构"""

        # 先得到树的层数
        def get_layer(node):
            """递归计算树的层数"""
            if node is None:
                return 0
            else:
                # 这里递归的核心是到叶节点的时候，叶节点的left和right都为None，所以返回0
                # 那么叶节点的上一层就是1
                left_depth = get_layer(node.left)
                right_depth = get_layer(node.right)
                return max(left_depth, right_depth) + 1

        layer = get_layer(self.__root)

        # 层序遍历并打印
        queue = deque([(self.__root, 1)])
        current_level = 1
        while queue:
            node, level = queue.popleft()
            if level > current_level:
                print()
                current_level += 1
            if node:
                print(f"{node.data:^{20 * layer // 2 ** (level - 1)}}", end="")
            else:
                print(f"{"N":^{20 * layer // 2 ** (level - 1)}}", end="")
            if level < layer:  # 如果当前节点不是最后一层（利用总深度做判断），才加入左右子节点
                if node:
                    # 如果当前节点不为空，将它的左右子节点加入队列
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
                else:
                    # 如果当前节点为空，将两个None加入队列
                    queue.append((None, level + 1))
                    queue.append((None, level + 1))
        print()
