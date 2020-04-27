'''
    236. 二叉树的最近公共祖先
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

    例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

    示例 1:

    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出: 3
    解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
    示例 2:

    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    输出: 5
    解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root, p, q):

        def recurse_tree(current_node):
            # 如果到达 空 子树，则返回 False
            if not current_node:
                return False
            
            # 遍历 左子树
            left = recurse_tree(current_node.left)

            # 遍历 右子树
            right = recurse_tree(current_node.right)

            # 判断当前节点 是不是 为 p 或 q 中的一个
            mid = current_node==p or current_node==q

            # 若 mid、left、right 三个中 有两个 为 True,那么表示找到 最近父节点
            if mid+left+right>=2:
                self.res = current_node
            
            return mid or left or right

        recurse_tree(root)
        return self.res
             
        
if __name__ == "__main__":
    
    tree = Tree()
    tree_p = Tree()
    tree_q = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        str3 = input()
        if str1 != "" and str2 != "" and str3 != "":
            node_list = str1.split(",")
            for node in node_list:
                tree.add(node)
            print(f"层次遍历：{tree.traverse(tree.root)}")

            p = tree.select(tree.root,int(str2))
            q = tree.select(tree.root,int(str3))
            res = solution.lowestCommonAncestor(tree.root,p,q)
            print(res)
        else:
            break
    






        


  