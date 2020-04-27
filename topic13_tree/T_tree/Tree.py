'''
    树实现

'''
from collections import deque
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Tree(object):
    def __init__(self):
        # 根节点定义为 root 永不删除，做为哨兵使用。
        self.root = None

    # 添加节点
    def add(self, x):
        node = Node(x)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    
    # 查找
    def select(self,root,x):
        if root is None:
            return None
        if root.val == x:
            return root
        left = self.select(root.left,x)
        if left is not None:
            return left
        right = self.select(root.right,x)
        if right is not None:
            return right
        return None


    # 先序遍历
    def preorder(self,root):
        if root is None:
            return []
        res = [root.val]
        left = self.preorder(root.left)
        right = self.preorder(root.right)
        return res+left+right

    # 中序遍历
    def inorder(self,root):
        if root is None:
            return []
        left = self.inorder(root.left)
        res = [root.val]
        right = self.inorder(root.right)
        return left+res+right

    # 后序遍历
    def postorder(self,root):
        if root is None:
            return []
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        res = [root.val]
        return left+right+res

    # 层次遍历
    def traverse(self,root):  
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque([root,])
        while queue:
            levels.append([])
            level_len = len(queue)
            for _ in range(level_len):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = level + 1
        return levels


if __name__ == "__main__":
    
    tree = Tree()
    node_list = [1,2,3,4,None,5,6]
    for node in node_list:
        tree.add(node)

    print(f"层次遍历：{tree.traverse(tree.root)}")
    print(f"前序遍历：{tree.preorder(tree.root)}")
    print(f"中序遍历：{tree.inorder(tree.root)}")
    print(f"后序遍历：{tree.postorder(tree.root)}")

    res = tree.select(tree.root,6)
    print(res)
    # while 1:
    #     str1 = input()
    #     str2 = input()
    #     if str1 != "" and str2 != "":
    #         board = [[c for c in s.split(",")] for s in str1.split(";")]
    #         words = str2.split(",")
    #         print(f"board:{board}")
    #         print(f"words:{words}")

    #         res = solution.findWords(board, words)
    #         print(res)
    #     else:
    #         break

