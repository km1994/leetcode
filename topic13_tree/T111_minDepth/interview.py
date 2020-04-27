'''
    # 111. 二叉树的最小深度

## 题目
### 介绍 

    给定一个二叉树，找出其最小深度。

  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

  说明: 叶子节点是指没有子节点的节点。

### 示例：
    
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回它的最小深度  2.
'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree


class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        children = [root.left,root.right]
        min_depth = 9999
        for c in children:
            if c:
                min_depth = min(self.minDepth(c),min_depth)
        return min_depth + 1

        
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

            res = solution.minDepth(tree.root)
            print(res)
        else:
            break
    






        


  