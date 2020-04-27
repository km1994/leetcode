'''
    466. 统计重复个数
    
    由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。

    如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。

    现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。

    请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。

     

    示例：

    输入：
        s1 ="acb",n1 = 4
        s2 ="ab",n2 = 2

    返回：
        2

'''
class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1==0:
            return 0
        s1_len = len(s1)
        s2_len = len(s2)
        s1_count = 0    # 经历多少s1
        s2_count = 0    # 经历多少s2
        p = 0           # 当前在s2的位置
        mp_dict = {}    # 记录每一次s1扫描结束后当前的状态，寻找循环
        while s1_count < n1:  
            for i in range(s1_len):  # 往前
                if s1[i] == s2[p]:
                    p = p + 1
                    if p == s2_len:  # s2扫描结束从头开始循环
                        p = 0
                        s2_count = s2_count + 1
            s1_count = s1_count + 1
            if p not in mp_dict:
                mp_dict[p] = [s1_count,s2_count]  # 记录当前状态
            else:    # 出现了循环 这次结束后p的位置和以前某一次一样，就是循环
                last = mp_dict.get(p)
                e1_circle = s1_count - last[0]
                e2_circle = s2_count - last[1]
                s2_count = s2_count + e2_circle * int((n1-s1_count)/e1_circle)
                s1_count = s1_count + e1_circle * int((n1-s1_count)/e1_circle)        # 更新他们
        return int(s2_count/n2)



if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        str3 = input()
        str4 = input()
        if str1 != "" and str2 != "" and str3 != "" and str4 != "":
            n1 = int(str3)
            n2 = int(str4)
            res = solution.getMaxRepetitions(str1,n1,str2,n2)
            print(res)
        else:
            break

