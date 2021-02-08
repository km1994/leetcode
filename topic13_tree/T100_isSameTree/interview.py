'''
    100. 相同的树

## 题目
### 介绍 

    给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree


class Solution:
    def isSameTree(self, p, q):
        '''
            解析：
                根据题意：如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
                该题 的不成立的三个点：
                    1.1. p.left 存在 q.left 不存在；
                    1.2. p.right 不存在 q.right 存在
                    1.3. p.val != q.val
                该题 的成立的点：
                    2.1. 所有 对应节点值 相等；
                    2.2. 每个节点 所包含的 子树一致
            思路：
                递归遍历两棵树：
                    1. 是否满足 前面 1.1 和 1.2：
                        满足：return False
                    2. 是否满足 2.1 和 2.2：
                        满足：return True
                    3. 是否满足 1.3：
                        满足：return False
                分别 向 p 和 q 的 左右子树 遍历
        '''
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True
        if p.val!=q.val:
            return False
        
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)) 

        
if __name__ == "__main__":
    
    tree1 = Tree()
    tree2 = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2!="":
            node_list1 = str1.split(",")
            node_list2 = str2.split(",")
            for node in node_list1:
                tree1.add(node)
            for node in node_list2:
                tree2.add(node)

            print(f"层次遍历：{tree1.traverse(tree1.root)}")
            print(f"层次遍历：{tree2.traverse(tree2.root)}")

            res = solution.isSameTree(tree1.root,tree2.root)
            print(res)
        else:
            break
    






        


  