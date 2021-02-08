'''
    124. 二叉树中的最大路径和
    给定一个非空二叉树，返回其最大路径和。

    本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

    示例 1:

    输入: [1,2,3]

       1
      / \
     2   3

    输出: 6
    示例 2:

    输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

    输出: 42

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree


class Solution:
    def maxPathSum(self, root):
        self.max_path_sum = float('-inf')
        def dfs(node):
            if not node:   # 边界情况
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cur_max = max(node.val,node.val+left,node.val+right)
            self.max_path_sum = max(self.max_path_sum,cur_max,node.val+left+right)
            return cur_max
        dfs(root)
        return self.max_path_sum
        
        
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

            res = solution.maxDepth(tree.root)
            print(res)
        else:
            break
    






        


  