'''
    3. 无重复字符的最长子串
    
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:

    输入: "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:

    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


'''
class Solution:
    # 方法一：滑动窗口法 1
    def lengthOfLongestSubstring1(self, s):
        s_len = len(s)
        # 哈希集合，记录每个字符是否出现过
        diff_set = set()
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        r = -1
        res = 0
        for i in range(s_len):
            if i!=0:
                # 左指针向右移动一格，移除一个字符
                diff_set.remove(s[i-1])
            while r+1 < s_len and s[r+1] not in diff_set:
                # 不断地移动右指针
                diff_set.add(s[r+1])
                r = r + 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            res = max(res,r-i+1)
        return res 

    # 方法一：滑动窗口法 2
    def lengthOfLongestSubstring2(self, s):
        if not s:return 0
        left = 0
        diff_dict = set()
        s_len = len(s)
        max_len = 0
        cur_len = 0
        for i in range(s_len):
            cur_len += 1
            while s[i] in diff_dict:
                diff_dict.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            diff_dict.add(s[i])
        return max_len


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.lengthOfLongestSubstring2(str1)
            print(res)
        else:
            break

