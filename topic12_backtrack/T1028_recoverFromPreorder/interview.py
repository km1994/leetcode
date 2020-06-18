'''
    1028. 从先序遍历还原二叉树

    我们从二叉树的根节点 root 开始进行深度优先搜索。

    在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

    如果节点只有一个子节点，那么保证该子节点为左子节点。

    给出遍历输出 S，还原树并返回其根节点 root。

    示例 1：
    输入："1-2--3--4-5--6--7"
    输出：[1,2,5,3,4,6,7]

    示例 2：
    输入："1-2--3---4-5--6---7"
    输出：[1,2,5,3,null,6,null,4,null,7]

    示例 3：
    输入："1-401--349---90--88"
    输出：[1,401,null,349,88,90]

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def recoverFromPreorder(self, S: str) -> TreeNode:
        tree = {}
        pos = 0
        while pos < len(S):
            depth = 0
            while S[pos] == '-':
                depth += 1
                pos += 1
            val = ''
            while pos < len(S) and S[pos]!= '-':
                val += S[pos]
                pos += 1
            if depth == 0:
                tree[0] = TreeNode(int(val))
            else:
                tree[depth] = TreeNode(int(val))
                if not tree[depth-1].left:
                    tree[depth-1].left = tree[depth]
                else:
                    tree[depth-1].right = tree[depth]
        return tree[0] if tree else None


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "" :
            res = solution.recoverFromPreorder(str1)
            print(res)
        else:
            break

