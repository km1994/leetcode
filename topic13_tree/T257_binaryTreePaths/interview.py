'''
    257. 二叉树的所有路径
    给定一个二叉树，返回所有从根节点到叶子节点的路径。

    说明: 叶子节点是指没有子节点的节点。

    示例:

    输入:

   1
 /   \
2     3
 \
  5

    输出: ["1->2->5", "1->3"]

    解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res

        def backtrack(root,res,path):
            path.append(root.val)
            if not root.left and not root.right:
                res.append("->".join(path))
                path.pop()
                return
            if root.left:
                backtrack(root.left,res,path)

            if root.right:
                backtrack(root.right,res,path)
            path.pop()

        backtrack(root,res,[])
        return res


if __name__ == "__main__":
    
    tree = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            node_list = [num for num in str1.split(",")]
            for node in node_list:
                tree.add(node)
            print(f"层次遍历：{tree.traverse(tree.root)}")

            res = solution.binaryTreePaths(tree.root)
            print(res)
        else:
            break
    






        


  