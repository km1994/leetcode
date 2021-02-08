'''
    637. 二叉树的层平均值

    给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。


示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。


'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree


class Solution:
    # 广度优先搜索
    def averageOfLevels(self, root) :
        averages = list()
        queue = collections.deque([root])
        while queue:
            total = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                left, right = node.left, node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            averages.append(total / size)
        return averages


    # 回溯法
    def averageOfLevels1(self, root):
        def dfs(root,level):
            if root:
                if level<len(totals):
                    totals[level] = totals[level]+root.val
                    counts[level] = counts[level]+1
                else:
                    totals.append(root.val)
                    counts.append(1)
                dfs(root.left,level+1)
                dfs(root.right,level+1)

        counts = []
        totals = []
        dfs(root,0)
        return [total / count for total, count in zip(totals, counts)]
        
if __name__ == "__main__":
    
    tree1 = Tree()
    tree2 = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            node_list1 = str1.split(",")
            for node in node_list1:
                tree1.add(node)

            print(f"层次遍历：{tree1.traverse(tree1.root)}")

            res = solution.averageOfLevels1(tree1.root)
            print(res)
        else:
            break
    






        


  