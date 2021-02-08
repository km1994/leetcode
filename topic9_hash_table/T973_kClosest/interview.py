'''
   973. 最接近原点的 K 个点

   我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

    （这里，平面上两点之间的距离是欧几里德距离。）

    你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

    示例 1：
        输入：points = [[1,3],[-2,2]], K = 1
        输出：[[-2,2]]
        解释： 
        (1, 3) 和原点之间的距离为 sqrt(10)，
        (-2, 2) 和原点之间的距离为 sqrt(8)，
        由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
        我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
    示例 2：
        输入：points = [[3,3],[5,-1],[-2,4]], K = 2
        输出：[[3,3],[-2,4]]
        （答案 [[-2,4],[3,3]] 也会被接受。）
    提示：
        1 <= K <= points.length <= 10000
        -10000 < points[i][0] < 10000
        -10000 < points[i][1] < 10000

'''
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 匿名函数：计算距离
        culEuclid = lambda point: math.sqrt(point[0]*point[0]+point[1]*point[1])
        # step 1:用于处理特殊情况， points_len <= K 和 K == 0 
        if K==0:
            return []
        points_len = len(points)
        if points_len <= K:
            return points
        # step 2：采用分桶的方式计算和存储 不同距离所包含的点的索引
        # 用于记录不同距离的索引列表
        cul_dist_dict = {}
        for i in range(points_len):
            temp = culEuclid(points[i])
            if temp not in cul_dist_dict:
                cul_dist_dict[temp] = []
            cul_dist_dict[temp].append(i)
        # step 3 : 字典排序
        cul_dist_dict = sorted(cul_dist_dict.items(),key=lambda x:x[0],reverse=False)
        # step 4 : 找出距离原点 最近 的 k 个点
        res = []
        for dis,pos_list in cul_dist_dict:
            for pos in pos_list:
                res.append(points[pos])
                K = K  - 1
                if K == 0:
                    return res

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and  str2 != "":
            nums = [int(num) for num in str1.split(",")]
            K = int(str2)
            res = solution.kClosest(nums,K)
            print(res)
        else:
            break

