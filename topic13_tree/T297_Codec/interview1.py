# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ''
        inorders = []
        preorders = []
        # 节点=>全局唯一标记映射字典
        maps = {}
        # 计数字典, 保存当前值接下来要用的编号
        indexdict = collections.defaultdict(int)

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            indexdict[node.val] += 1
            # 保存全局唯一节点标记字符串
            uniquestr = str(node.val) + ';' + str(indexdict[node.val])
            inorders.append(uniquestr)
            maps[node] = uniquestr
            inorder(node.right)

        def preorder(node):
            if not node:
                return
            # 这里直接用存储好的标记字符串即可
            preorders.append(maps[node])
            preorder(node.left)
            preorder(node.right)

        inorder(root)
        preorder(root)

        return ','.join(preorders)+'+'+','.join(inorders)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        preorders, inorders = data.split('+')
        preorders = preorders.split(',')
        inorders = inorders.split(',')
        n = len(preorders)
        # 存储标记值到中序遍历下标的映射
        vtoi = {}
        for i, uniquestr in enumerate(inorders):
            vtoi[uniquestr] = i

        def build(pb, pe, ib, ie):
            # 经典递归, 从前序和中序序列中构造二叉树
            if pb > pe:
                return None
            uniquestr = preorders[pb]
            val = int(uniquestr.split(';')[0])
            root = TreeNode(val)
            if pb == pe:
                return root
            # 得到中序遍历序列中对应根节点的下标
            im = vtoi[preorders[pb]]
            pm = im-ib+pb
            root.left = build(pb+1, pm, ib, im-1)
            root.right = build(pm+1, pe, im+1, ie)
            return root
        return build(0, n-1, 0, n-1)
