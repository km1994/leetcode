'''
    98. 验证二叉搜索树
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。

    假设一个二叉搜索树具有如下特征：

    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    示例 1:

    输入:
    2
   / \
  1   3
    输出: true
    示例 2:

    输入:
    5
   / \
  1   4
     / \
    3   6
    输出: false
    解释: 输入为: [5,1,4,null,null,3,6]。
         根节点的值为 5 ，但是其右子节点值为 4 。

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def isValidBST(self, root):
         #中序遍历，观察到中序遍历的顺序是左->中->右,也就是按照从小到大的顺序，因此这样思考题目就很好解了,按照中序遍历，将值依次存入列表中。最后判断
        if not root:
            return True
        result = []
        def middle_traversal(root):
            if root.left:
                middle_traversal(root.left)
            result.append(root.val)
            if root.right:
                middle_traversal(root.right)
        middle_traversal(root)
        return result == sorted(result) and len(set(result)) == len(result)
        
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

            res = solution.isValidBST(tree.root)
            print(res)
        else:
            break
    






        


  