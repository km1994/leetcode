'''
    572. 另一个树的子树
    给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

    示例 1:
    给定的树 s:

     3
    / \
   4   5
  / \
 1   2
    给定的树 t：

   4 
  / \
 1   2
    返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

    示例 2:
    给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
    给定的树 t：

   4
  / \
 1   2
    返回 false。

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def isSubtree(self, s, t):
        return self.backtrack(s,t)

    def backtrack(self,s,t):
        if not s:
            return False
        return self.check(s,t) or self.backtrack(s.left,t) or self.backtrack(s.right,t)

    def check(self,s,t):
        if not s and not t:
            return True
        if (not s and t) or (s and not t) or (s.val!=t.val):
            return False
        return self.check(s.left,t.left) and self.check(s.right,t.right)

        
if __name__ == "__main__":
    
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2!="":
            s_tree = Tree()
            t_tree = Tree()
            s_node_list = [int(num) for num in str1.split(",")]
            for node in s_node_list:
                s_tree.add(node)
            t_node_list = [int(num) for num in str2.split(",")]
            for node in t_node_list:
                t_tree.add(node)
            print(f"层次遍历：{s_tree.traverse(s_tree.root)}")
            print(f"层次遍历：{t_tree.traverse(t_tree.root)}")

            res = solution.isSubtree(s_tree.root,t_tree.root)
            print(res)
        else:
            break
    






        


  