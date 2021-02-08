'''
    面试题 16.11. 跳水板
    你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

    返回的长度需要从小到大排列。

    示例：

        输入：
            shorter = 1
            longer = 2
            k = 3
        输出： {3,4,5,6}

'''

# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 动态规划法
    def divingBoard(self, shorter: int, longer: int, k: int):
        if not k:
            return []
        if shorter == longer:
            return [k*shorter]
        res = [k*shorter]
        dif = longer-shorter
        for __ in range(k):
            res.append(res[-1]+dif)
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        str3 = input()
        if str1 != "" and str2!="" and str3!="":
            shorter = int(str1)
            longer = int(str2)
            k = int(str3)
            res = solution.divingBoard(shorter,longer,k)
            print(res)
        else:
            break

