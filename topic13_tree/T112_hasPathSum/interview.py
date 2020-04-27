'''
    112. 路径总和
    给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

    说明: 叶子节点是指没有子节点的节点。

    示例: 
    给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
    返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        left = self.hasPathSum(root.left,sum-root.val)
        right = self.hasPathSum(root.right,sum-root.val)
        return left or right
        
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
    






        


  