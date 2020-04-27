'''
    113. 路径总和 II
    给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

    说明: 叶子节点是指没有子节点的节点。

    示例:
    给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
    返回:

    [
        [5,4,11,2],
        [5,8,4,5]
    ]

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def pathSum(self, root, sum):
        res = []

        def backtrack(root,path,sum):
            path.append(root.val)
            if not root.left and not root.right:
                if root.val == sum:
                    res.append(path[:])
                path.pop()
                return 
            if root.left:
                backtrack(root.left,path,sum-root.val)
            if root.right:
                backtrack(root.right,path,sum-root.val)
            path.pop()

        if not root:
            return res
        backtrack(root,[],sum)
        return res

        
if __name__ == "__main__":
    
    tree = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "":
            node_list = [int(num) for num in str1.split(",")]
            for node in node_list:
                tree.add(node)
            sum = int(str2)
            print(f"层次遍历：{tree.traverse(tree.root)}")

            res = solution.hasPathSum(tree.root,sum)
            print(res)
        else:
            break
    






        


  