'''
    406. 根据身高重建队列

    假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

    注意：
    总人数少于1100人。

    示例

    输入:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    输出:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

'''
class Solution:
    def reconstructQueue(self, people):
        res = []
        # step 1：按 h 倒序排序，按 k 正序排序
        people = sorted(people, key= lambda x : (x[0],-x[1]),reverse=True)
        # step 2: 按 k 插入 数组对应位置
        for p in people:
            res.insert(p[1],p)
        return res

    def econstructQueue1(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        ans = list()
        for person in people:
            print(person)
            ans[person[1]:person[1]] = [person]
        return ans
if __name__ == "__main__":
    
    solution = Solution()
    print("-----------1-----------")
    nums = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    res = solution.econstructQueue(nums)
    print(res)


    


    







        


  