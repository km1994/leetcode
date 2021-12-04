'''
    700. 二叉搜索树中的搜索
    
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
你应该返回如下子树:

      2     
     / \   
    1   3


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
            :type root: TreeNode
            :type val: int
            :rtype: TreeNode
            方法：递归查找
            解析：
                本题突破点：该树 为 二叉搜索树（BST）
                    左子树.val 小于 root.val
                    右子树.val 大于 root.val
        """
        # 判空
        if not root:
            return None 
  
        if root.val>val:    # 目标子树 可能在 左子树
            return self.searchBST(root.left,val)
        elif root.val<val:  # 目标子树 可能在 右子树
            return self.searchBST(root.right,val)
        else:                # 找到 目标子树
            return root