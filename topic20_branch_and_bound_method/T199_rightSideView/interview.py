'''
    【广度优先搜索】199.二叉树的右视图

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。


示例:


输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:


   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
            方法：队列迭代 (非递归)
        '''
        res = []
        if not root:
            return res 
        queue = collections.deque()
        queue.append(root)
        while queue:
            last = -999
            for i in range(len(queue)):
                node = queue.popleft()
                last = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(last)
        return res