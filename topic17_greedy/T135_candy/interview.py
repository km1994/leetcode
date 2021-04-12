class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
            方法：贪心算法
            思路：
                1. 先从左至右遍历学生成绩 ratings，按照以下规则给糖，并记录在 left 中：
                    1. 先给所有学生 11 颗糖；
                    2. 若 ratingsi >ratingsi−1，则第 ii 名学生糖比第 i - 1i−1 名学生多 11 个。
                    3. 若 ratingsi<=ratingsi−1，则第 ii 名学生糖数量不变。（交由从右向左遍历时处理。）
                    经过此规则分配后，可以保证所有学生糖数量 满足左规则 。
                2. 同理，在此规则下从右至左遍历学生成绩并记录在 right 中，可以保证所有学生糖数量 满足右规则 。
                3. 最终，取以上 22 轮遍历 left 和 right 对应学生糖果数的 最大值 ，这样则 同时满足左规则和右规则 ，即得到每个同学的最少糖果数量。
        '''
        ratings_len = len(ratings)
        if ratings==0:
            return 0
        left = []
        right = []
        for _ in range(ratings_len):
            left.append(1)
            right.append(1)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: left[i] = left[i - 1] + 1
        
        res = left[-1]
        for i in range(ratings_len-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
            res = res+max(left[i],right[i])
        return res