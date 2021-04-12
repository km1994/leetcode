# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
            解析：因为 node 的节点值 是要删除的节点值
            思路：
                step 1 将 node.next 值 覆盖 node 值
                step 2：记录当前节点，方便后期删除
                step 3：指针移动
            复杂度：
                时间：O(1)
                空间：O(1)
        """
        # step 1 将 node.next 值 覆盖 node 值
        node.val = node.next.val 
        # step 2：记录当前节点，方便后期删除
        tmp_node = node.next
        # step 3：指针移动
        node.next = node.next.next  
        del tmp_node         # 删除节点，防止泄露