'''
    93. 复原IP地址
    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

    有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

    例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

     

    示例 1：

    输入：s = "25525511135"
    输出：["255.255.11.135","255.255.111.35"]
    示例 2：

    输入：s = "0000"
    输出：["0.0.0.0"]
    示例 3：

    输入：s = "1111"
    输出：["1.1.1.1"]
    示例 4：

    输入：s = "010010"
    输出：["0.10.0.10","0.100.1.0"]
    示例 5：

    输入：s = "101023"
    输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

'''
import copy
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    def restoreIpAddresses(self, s):
        s_len = len(s)
        res = []
        # step 1：判断字符串 长度 是否 在 [5,12]
        if s_len<4 or s_len >12:
            return res 
        # step 2：回溯法
        path = []
        self.dfs(s,s_len,0,0,path,res)
        return res
    # 功能：回溯法
    def dfs(self,s,s_len,split_times,begin,path,res):
        # begin 指针 移动 到 尾部
        if begin==s_len:
            # 判断 分割次数 是否 等于 4
            if split_times==4:
                res.append(".".join(path))
            return 
        # 判断 剩余长度 是否 在 [(4-split_times),3*(4-split_times)]
        if s_len-begin<(4-split_times) or s_len-begin>3*(4-split_times):
            return
        # 因为 每一个地址单元 长度 在 [0,255]，所以 每 1-3 为一个 单元
        for i in range(3):
            if begin+i>=s_len:
                break
            now_seg = self.valid(begin,begin+i,s)
            if now_seg!=-1:
                path.append(str(now_seg))
                self.dfs(s,s_len,split_times+1,begin+i+1,path,res)
                path.pop()
    # 功能：验证 字符串 是否合格 函数，即 [0,255] 内
    def valid(self, left,right,s):
        num = 0
        for i in range(left,right+1):
            if left!=right and s[left]=="0":
                return -1
            num = num*10+int(s[i])
            if num>255:
                return -1
        return num

    
if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.restoreIpAddresses(str1)
            print(res)
        else:
            break

