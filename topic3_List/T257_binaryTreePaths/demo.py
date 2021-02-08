'''
    257. 二叉树的所有路径
    给定一个二叉树，返回所有从根节点到叶子节点的路径。

    说明: 叶子节点是指没有子节点的节点。

    示例:

    输入:

   1
 /   \
2     3
 \
  5

    输出: ["1->2->5", "1->3"]

    解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def backtrack(root,path):
            if root:
                path = path+str(root.val)
                if not root.left and not root.right:
                    res.append(path)
                path = path + "->"
                backtrack(root.left,path)
                backtrack(root.right,path)
        backtrack(root,"")
        return res

if __name__ == "__main__":
    l1 = arr2List([1,2,4,5,6,8,9])
    print_list(l1)
    solution = Solution()
    res = solution.binaryTreePaths(l1)

    print_list(res)
    






        


  