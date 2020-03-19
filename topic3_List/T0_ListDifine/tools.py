'''
    21. 合并两个有序链表
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

    示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 功能：列表转链表
def arr2List(arr_list):
    '''
    列表转链表
    :param arr_list: List  列表
    :return:
        ln_head： ListNode  链表
    '''
    if len(arr_list)>0:
        ln_head = ListNode(arr_list[0])
        p = ln_head
        for i in range(1,len(arr_list)):
            ln = ListNode(arr_list[i])
            p.next =ln
            p=p.next
    return ln_head

# 功能：输出链表
def print_list(ln_head):
    '''
    输出链表
    :param ln_head:  listNode   链表
    :return:

    '''
    print("--------Print List-------")
    i = 0
    while ln_head:
        print("ln[{0}].val:{1}".format(i,ln_head.val))
        ln_head = ln_head.next
        i = i + 1



if __name__ == "__main__":
    
    arr1 = [9,1,6,3]
    list1 = arr2List(arr1)
    print_list(list1)
    







        


  