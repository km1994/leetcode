'''
    95. 不同的二叉搜索树 II
    给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

    示例：

    输入：3
    输出：
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    解释：
    以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        dct = {}

        def left_right(left, right):
            if left > right:
                return [None]
            if (left, right) in dct:
                return dct[(left, right)]
            ret = []
            for i in range(left, right+1):
                left_lst = left_right(left, i-1)
                right_lst = left_right(i+1, right)
                for L in left_lst:
                    for R in right_lst:
                        app_Tree = Tree(i)
                        app_Tree.left = L
                        app_Tree.right = R
                        ret.append(app_Tree)
            dct[(left, right)] = ret
            return ret
        return left_right(1, n)

        
# if __name__ == "__main__":
    
#     tree = Tree()
#     solution = Solution()
#     while 1:
#         str1 = input()
#         if str1 != "":
#             n = int(str1)
#             res = solution.generateTrees(n)
#             for r in res:
#                 print(f"层次遍历：{tree.traverse(r.root)}")
#         else:
#             break
    






        


  