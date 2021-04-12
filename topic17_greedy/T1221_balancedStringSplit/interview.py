class Solution:
    def balancedStringSplit(self, s: str) -> int:
        '''
            方法：贪心算法
            思路：
                1. 定义一个 结果变量 res 和一个 状态变量 num
                2. 判断字符：
                    2.1 if 是 R，num = num - 1
                    2.2 if 是 L，num = num + 1
                3. 如果 num == 0，res = res+1
        '''
        res = 0 
        num = 0
        for c in s:
            if c=="R":
                num=num-1
            elif c=="L":
                num=num+1
            if num == 0:
                res=res+1
        return res