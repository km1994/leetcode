'''
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：

        输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
        输出：7 -> 0 -> 8
        原因：342 + 465 = 807
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    '''
        方法一 begin
    '''
    # 功能： 将给定两个列表进行合并
    def addTwoNumbers1(self, l1, l2):
        '''
        将给定两个列表进行合并
        :param l1: ListNode
        :param l2: ListNode
        :return:
            res_ln：List   合并后的列表
        '''
        num=0
        digits=1
        while l1 and l2:
            #print("l1.val:{0}".format(l1.val))
            #print("l2.val:{0}".format(l2.val))
            num = (l1.val + l2.val) * digits + num
            digits = digits * 10
            l1 = l1.next
            l2 = l2.next

        num = self.list_not_end( l1, num, digits)
        num = self.list_not_end( l2, num, digits)
        print("num:{0}".format(num))
        res_list = self.num2List(num)
        return res_list

    # 功能： 如果一边的列表还不为空，需要进行对他进行遍历，直到结束
    def list_not_end(self,list,num,digits):
        '''
        如果一边的列表还不为空，需要进行对他进行遍历，直到结束
        :param list:    不为空的列表
        :param num:     叠加之后的结果
        :param digits:  10的倍数，主要用于记录当前位
        :return:
        '''
        while list:
            #print("list.val:{0}".format(list.val))
            num = (list.val) * digits + num
            digits = digits * 10
            list = list.next
        return num

    # 功能： 将数字转化为所对应的列表
    def num2List(self,num):
        '''
        功能： 将数字转化为所对应的列表
        :param num:  数字
        :return:
            ln ：  List   转化后的列表
        '''
        print("---------------")
        l =[]
        if num == 0:
            l.append(num)
        else:
            while num !=0:
                #print("num:{0}".format(num))
                numDigits = num % 10
                l.append(numDigits)
                num = int(num / 10)
        #print("ln:{0}".format(ln))
        return l

    '''
        方法一 end
    '''

    '''
        方法二 begin
    '''
    # 功能： 将给定两个列表进行合并
    def addTwoNumbers2(self, l1, l2):
        jinwei=0
        num = 0
        ln_head=ListNode(0)
        p = ln_head
        while l1 and l2:
            if jinwei == 1:
                num = l1.val + l2.val + 1
                if num >= 10:
                    num = num % 10
                    jinwei = 1
                else:
                    jinwei=0
            else:
                num = l1.val + l2.val
                if num >= 10:
                    num = num % 10
                    jinwei = 1
                else:
                    jinwei=0

            ln = ListNode(num)
            p.next = ln
            p=p.next
            l1=l1.next
            l2 = l2.next

        # 若链表 l1 不为空，将后面部分加到链表 p 上面
        while l1:
            if jinwei == 1:
                num = l1.val  + 1
                if num >= 10:
                    num = num % 10
                    jinwei = 1
                else:
                    jinwei = 0
                ln = ListNode(num)
                p.next = ln
                p = p.next
            else:
                p.next = l1
                p = p.next
            l1=l1.next

        # 若链表 l2 不为空，将后面部分加到链表 p 上面
        while l2:
            if jinwei == 1:
                num = l2.val  + 1
                if num >= 10:
                    num = num % 10
                    jinwei = 1
                else:
                    jinwei = 0
                ln = ListNode(num)
                p.next = ln
                p = p.next
            else:
                p.next = l2
                p=p.next
            l2 = l2.next

        if jinwei == 1:
            ln = ListNode(1)
            p.next = ln

        ln_head = ln_head.next
        arr = self.list2arr(ln_head)
        return arr

    # listnode to arr(list)
    def list2arr(self,list):
        '''
        功能：链表 to 列表
        :param list: listnode   链表
        :return:
            arr： list  列表
        '''
        p = list
        arr=[]
        while p:
            arr.append(p.val)
            p = p.next
        return arr

    '''
        方法二 begin
    '''

    '''
        工具方法 begin
    '''

    # 功能：列表转链表
    def arr2List(self,arr_list):
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
    def print_list(self,ln_head):
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

    '''
        工具方法 end
    '''

if __name__ == "__main__":
    arr1 = [9,1,6,3]
    arr2 = [0]

    solution = Solution()

    ln1 = solution.arr2List(arr1)
    ln2 = solution.arr2List(arr2)

    # solution.print_list(ln1)
    # solution.print_list(ln2)

    # res_list = solution.addTwoNumbers1(ln1,ln2)
    #
    # print("arr1:{0}".format(arr1))
    # print("arr2:{0}".format(arr2))
    # print("to")
    # print("res_list:{0}".format(res_list))

    res_list = solution.addTwoNumbers2(ln1, ln2)

        


  