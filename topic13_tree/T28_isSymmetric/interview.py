'''
    面试题28. 对称的二叉树
    请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

    示例 1：

    输入：root = [1,2,2,3,4,4,3]
    输出：true
    示例 2：

    输入：root = [1,2,2,null,3,null,3]
    输出：false

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.symmetry(root.left,root.right)
    
    def symmetry(self,left,right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.symmetry(left.left,right.right) and self.symmetry(left.right,right.left)
        
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

            res = solution.isSymmetric(tree.root)
            print(res)
        else:
            break
    






        


  