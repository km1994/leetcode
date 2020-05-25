'''
    1010. 总持续时间可被 60 整除的歌曲

    在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

    返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。

    示例 1：

    输入：[30,20,150,100,40]
    输出：3
    解释：这三对的总持续时间可被 60 整数：
    (time[0] = 30, time[2] = 150): 总持续时间 180
    (time[1] = 20, time[3] = 100): 总持续时间 120
    (time[1] = 20, time[4] = 40): 总持续时间 60
    示例 2：

    输入：[60,60,60]
    输出：3
    解释：所有三对的总持续时间都是 120，可以被 60 整数。

'''
import collections 
class Solution:
    def fourSumCount1(self, time):
        res = 0
        time_dict = collections.defaultdict(int)
        for t in time:
            t = t%60
            if t in time_dict:
                res = res + time_dict[t]
            
            if t == 0:
                time_dict[t] +=1
                continue

            time_dict[60- t] += 1
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums1 = [int(num) for num in str1.split(",")]
            res = solution.fourSumCount1(nums1)
            print(res)
        else:
            break

