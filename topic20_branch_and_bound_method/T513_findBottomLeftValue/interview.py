'''
    【广度优先搜索】513.找树左下角的值

    给定一个二叉树，在树的最后一行找到最左边的值。


示例 1:


输入:


    2
   / \
  1   3


输出:
1
 


示例 2:


输入:


        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7


输出:
7

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        '''
            方法：队列迭代 (层次遍历非递归)
        '''
        # step 1:判空
        res = -1
        if not root:
            return res 
        # step 2: 初始化队列
        queue = collections.deque()
        queue.append(root)
        # step 3：层次遍历 非递归法
        while queue:
            # step 4:每一层做遍历
            for i in range(len(queue)):
                node = queue.popleft()
                #  step 5:每一层 第一个元素
                if i==0:
                    res = node.val
                # step 6：root 的 左子树 入队
                if node.left:
                    queue.append(node.left)
                # step 7：root 的 右子树 入队
                if node.right:
                    queue.append(node.right)     
        return res