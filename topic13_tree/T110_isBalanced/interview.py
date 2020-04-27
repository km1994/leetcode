'''
    110. 平衡二叉树
    给定一个二叉树，判断它是否是高度平衡的二叉树。

    本题中，一棵高度平衡二叉树定义为：

    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

    示例 1:

    给定二叉树 [3,9,20,null,null,15,7]

     3
    / \
   9  20
     /  \
    15   7
    返回 true 。

    示例 2:

    给定二叉树 [1,2,2,3,3,null,null,4,4]

         1
        / \
       2   2
     / \
    3    3
    / \
   4   4
    返回 false 。

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def get_height(self,root):
        if not root:
            return -1
        return 1+max(self.get_height(root.left),self.get_height(root.right))

    def isBalanced(self, root):
        if not root:
            return True

        if abs(self.get_height(root.left)-self.get_height(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
       
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

            res = solution.isBalanced(tree.root)
            print(res)
        else:
            break
    






        


  