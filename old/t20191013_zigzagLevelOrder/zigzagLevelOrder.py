#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/10/13
@url：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
@desc:
    
    103. 二叉树的锯齿形层次遍历

    给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

    例如：
    给定二叉树 [3,9,20,null,null,15,7],

        3
    / \
    9  20
        /  \
    15   7
    返回锯齿形层次遍历如下：

    [
    [3],
    [20,9],
    [15,7]
    ]

'''
import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return res
        
        queue = []
        
        queue.insert(0,root)
        isReverse = False
        while queue:
            curLevel = []
            for _ in range(len(queue)):
                cur = queue.pop()
                if cur.left:
                    queue.insert(0,cur.left)

                if cur.right:
                    queue.insert(0,cur.right)

                if isReverse:
                    curLevel.insert(0,cur.val)
                else:
                    curLevel.append(cur.val)
                    
            isReverse = not isReverse
            res.append(curLevel)
        return res

if __name__ == "__main__":

    solution = Solution()

    # print("--------1-------")
    # nums1 = "Let's take LeetCode contest"
    # res=solution.reverseWords(nums1)
    # print("res:{0}".format(res))

    res = [1,2]
    res.append(3)
    res.insert(0,1)
    print(res)

    print(res.pop())
    print(res)

    res1 = []

    if not res1:
        print("aa")


    a = set()
    a.add(1)
    a.add(2)
    a.add(1)
    print(a)







    

    