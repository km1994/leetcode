'''
    763. 划分字母区间

    字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

    示例 1：

        输入：S = "ababcbacadefegdehijhklij"
        输出：[9,7,8]
        解释：
        划分结果为 "ababcbaca", "defegde", "hijhklij"。
        每个字母最多出现在一个片段中。
        像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

'''
class Solution:
    # 贪心算法 + 双指针
    def partitionLabels(self, S):
        '''
            方法：贪心算法 + 双指针
            思路：
                1. 利用 字典 记录 每个 字符 最后一次出现的下标位置；
                2. 定义 start 和 end 用于维护 当前片段区间，定义 char_max_pos 用于记录 最远位置；
                3. 遍历字符串：
                    3.1 比较当前字符 最后一次出现位置 和 最远距离 char_max_pos 的大小，将最大的赋予 char_max_pos；
                    3.2 若 end 和 char_max_pos 相等，则表示以 start 和 end 为边界的 切片 包含前面出现过的所有字符的最远位置：
                        3.2.1 记录，并 切片；
                        3.2.2 新片 从 上一次切片 的 下一个位置开始；
        '''
        # 利用哈希表 记录 每个字符 出现 的最远位置
        last_char_pos_dict = {}
        S_len = len(S)
        for i in range(S_len):
            last_char_pos_dict[S[i]] = i
        # 定义 双指针
        start = end = 0
        # 记录 最远位置
        char_max_pos = 0
        res = []
        # 遍历字符串
        while end < S_len:
            # 当前字符 出现的最远位置
            cur_char_max_pos = last_char_pos_dict[S[end]]
            # 比较 当前字符的最远位置 和 历史最远位置，去 最远位置，目的是为了保证 该区间能够覆盖所有字符
            char_max_pos = max(cur_char_max_pos,char_max_pos)
            # 如果 end 遍历 到最远位置，那么他即可包含前面出现过的所有字符的最远位置
            if end == char_max_pos:
                # 切片
                res.append(end-start+1)
                # 新片 从 上一次切片 的 下一个位置开始
                start = end+1
            end = end+1
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.partitionLabels(str1)
            print(res)
        else:
            break

