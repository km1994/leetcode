'''
    129. 求根到叶子节点数字之和
    给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

    例如，从根到叶子节点路径 1->2->3 代表数字 123。

    计算从根到叶子节点生成的所有数字之和。

    说明: 叶子节点是指没有子节点的节点。

    示例 1:

    输入: [1,2,3]
    1
   / \
  2   3
    输出: 25
    解释:
    从根到叶子节点路径 1->2 代表数字 12.
    从根到叶子节点路径 1->3 代表数字 13.
    因此，数字总和 = 12 + 13 = 25.
    示例 2:

    输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
    输出: 1026
    解释:
    从根到叶子节点路径 4->9->5 代表数字 495.
    从根到叶子节点路径 4->9->1 代表数字 491.
    从根到叶子节点路径 4->0 代表数字 40.
    因此，数字总和 = 495 + 491 + 40 = 1026.

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def sumNumbers(self, root):
        self.res = 0
        def backtrack(root,temp_sum):
            temp_sum = temp_sum*10 + root.val
            if not root.left and not root.right:
                self.res = self.res + temp_sum
                temp_sum = int((temp_sum-root.val)/10) 
                return 
            if root.left:
                backtrack(root.left,temp_sum)
            if root.right:
                backtrack(root.right,temp_sum)
            temp_sum = int((temp_sum-root.val)/10) 

        if not root:
            return self.res
        backtrack(root,0)
        return self.res

        
if __name__ == "__main__":
    
    tree = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            node_list = [int(num) for num in str1.split(",")]
            for node in node_list:
                tree.add(node)
            print(f"层次遍历：{tree.traverse(tree.root)}")

            res = solution.sumNumbers(tree.root)
            print(res)
        else:
            break
    






        


  