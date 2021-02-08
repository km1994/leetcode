'''
    538. 把二叉搜索树转换为累加树
    给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。


    例如：

    输入: 原始二叉搜索树:
              5
            /   \
           2     13
    输出: 转换为累加树:
             18
            /   \
          20     13


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
    res = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convertBST(root.right)
        self.res =self.res+root.val
        root.val =self.res
        self.convertBST(root.left)
        return root
        
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
            res = solution.convertBST(tree.root)
            print(res)
        else:
            break
 
  