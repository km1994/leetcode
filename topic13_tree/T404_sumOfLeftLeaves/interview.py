'''
    404. 左叶子之和
    计算给定二叉树的所有左叶子之和。

    示例：

    3
   / \
  9  20
    /  \
   15   7

    在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

'''
import sys
sys.path.append("..") # 这句是为了导入_config
from T_tree.Tree import Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        return self.dfs(root)

    def dfs(self,root):
        res = 0
        if root.left:
            if self.isLeafNode(root.left):
                res = res + root.left.val
            else:
                res = res+self.dfs(root.left)
        if root.right and not self.isLeafNode(root.right):
            res = res+self.dfs(root.right)
        return res

    def isLeafNode(self,node):
        return not node.left and not node.right
        
if __name__ == "__main__":
    tree = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            node_list = str1.split(",")
            for node in node_list:
                tree.add(node)
            print(f"层次遍历：{tree.traverse(tree.root)}")
            res = solution.sumOfLeftLeaves(tree.root)
            print(res)
        else:
            break
 
  