'''
    230. 二叉搜索树中第K小的元素
    给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

    说明：
    你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

    示例 1:

    输入: root = [3,1,4,null,2], k = 1
     3
    / \
   1   4
    \
     2
    输出: 1
    示例 2:

    输入: root = [5,3,6,2,4,null,null,1], k = 3
        5
        / \
       3   6
      / \
     2   4
    /
   1
    输出: 3

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree


class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


if __name__ == "__main__":
    
    tree = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            node_list = str1.split(",")
            for node in node_list:
                tree.add(node)
            print(f"层次遍历：{tree.traverse(tree.root)}")

            k = int(str2)

            res = solution.kthSmallest(tree.root,k)
            print(res)
        else:
            break
    






        


  