'''
    剑指 Offer 07. 重建二叉树

    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

    例如，给出

    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
sys.path.append("..") # 这句是为了导入_config
from T_tree.Tree import Tree
class Solution:
    def buildTree(self, preorder, inorder):
        '''
            方法： 分治算法
            背景知识：
                前序遍历 List 特点：[ 根 | 左子树 | 右子树 ]
                中序遍历 List 特点：[  左子树 | 根 |右子树 ] 
            解析：
                根据 题目 所给出的条件：
                     前序遍历 ： 可以 获取 到 二叉树 的 根节点 （首位置）；
                     中序遍历 ： 可以 结合 前序遍历 的 根节点，对 二叉树 进行 左右分割；
                最后 通过 不断 切分 即可 构建 一个 完整 的 二叉树
            思路：
                1. 利用 前序遍历 获得 根节点；
                2. 以 中序遍历 中 根节点 的 位置，将 中序遍历 列表 分成 左右子树；
                3. 分别 对 左右子树 进行 1-2 步 操作，直到 遇到叶子节点，则向上返回；
        '''
        # step 1 : 构建 中序遍历搜索字典。 因为 我们 需要 确定 根节点 在 中序遍历 中的位置，而且为了提高搜索效率，采用字典反向映射
        inorderDict = {}                 
        inorderLen = len(inorder)        
        for i in range(inorderLen):     
            inorderDict[inorder[i]] = i 
        # step 2 : 以 根节点 为 中心，遍历左右子树
        return self.recursion(0,0,inorderLen-1,inorderDict,preorder)

    # 分治 构建 子二叉树
    def recursion(self,root,left,right,inorderDict,preorder):
        # step 1 : 判定 是否 到达 叶子节点
        if left>right:
            return 
        # step 2 : 构建根节点
        node = Tree(preorder[root])
        # step 3 : 搜索 根节点 在 中序遍历 中 的位置
        index = inorderDict[preorder[root]]
        # step 4 : 分割 左右子树
        node.left = self.recursion(root+1,left,index-1,inorderDict,preorder)
        node.right = self.recursion(index-left+root+1,index+1,right,inorderDict,preorder)
        return node 
        
if __name__ == "__main__":
    tree1 = Tree()
    tree2 = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2!="":
            preorder = str1.split(",")
            inorder = str2.split(",")
            res = solution.buildTree(preorder, inorder)
            print(res)
        else:
            break
    