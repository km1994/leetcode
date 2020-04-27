'''
    563. 二叉树的坡度
    给定一个二叉树，计算整个树的坡度。

    一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

    整个树的坡度就是其所有节点的坡度之和。

    示例:

    输入: 
          1
        /   \
       2     3
    输出: 1
    解释: 
    结点的坡度 2 : 0
    结点的坡度 3 : 0
    结点的坡度 1 : |2-3| = 1
    树的坡度 : 0 + 0 + 1 = 1

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

class Solution:
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root):
        self.traverse(root)
        return self.tilt
        
    
    def traverse(self,root):
        if root is None:
            return 0
        left_height = self.findTilt(root.left)
        right_height = self.findTilt(root.right)
        self.tilt += int(math.fabs(left_height-right_height))
        return left_height+right_height+root.val
        
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

            res = solution.findTilt(tree.root)
            print(res)
        else:
            break
    






        


  