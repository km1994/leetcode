'''
    57. 插入区间

    给出一个无重叠的 ，按照区间起始端点排序的区间列表。

    在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

    示例 1:

    输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
    输出: [[1,5],[6,9]]
    示例 2:

    输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    输出: [[1,2],[3,10],[12,16]]
    解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

'''
class Solution:
    def insert(self, intervals, newInterval):
        res = []
        flag = False
        intervals_len = len(intervals)
        for i in range(intervals_len):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                continue
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                flag = not flag
                for j in range(i,intervals_len):
                    res.append(intervals[j])
                break
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
        if not flag:
            res.append(newInterval)
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            intervals = [[int(c) for c in s.split(",")] for s in str1.split(";")]
            newInterval = [int(c) for c in str2.split(",")]
            res = solution.insert(intervals, newInterval)
            print(res)
        else:
            break

