'''
    94. 二叉树的中序遍历
    给定一个二叉树，返回它的中序 遍历。

    示例:

    输入: [1,null,2,3]
   1
    \
     2
    /
   3

    输出: [1,3,2]

'''
import sys
sys.path.append("..") # 这句是为了导入_config
from T_tree.Tree import Tree
import math
class Solution:
    def inorderTraversal(self, root):
        res = []
        def dfs(root):
            if root:
                if root.left:
                    dfs(root.left)
                res.append(root.val)
                if root.right:
                    dfs(root.right)
        dfs(root)
        return res
        
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
            res = solution.inorderTraversal(tree.root)
            print(res)
        else:
            break
    






        


  