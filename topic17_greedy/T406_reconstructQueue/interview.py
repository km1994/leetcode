class Solution:
    def reconstructQueue(self, people):
        res = []
        # step 1：按 h 倒序排序，按 k 正序排序
        people = sorted(people, key= lambda x : (x[0],-x[1]),reverse=True)
        # step 2: 按 k 插入 数组对应位置
        for p in people:
            res.insert(p[1],p)
        return res



