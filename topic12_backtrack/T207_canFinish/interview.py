'''
    207. 课程表
    你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

    在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

    给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

     

    示例 1:

    输入: 2, [[1,0]] 
    输出: true
    解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
    示例 2:

    输入: 2, [[1,0],[0,1]]
    输出: false
    解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
     

    提示：

    输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
    你可以假定输入的先决条件中没有重复的边。
    1 <= numCourses <= 10^5

'''
import copy
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def canFinish(self, numCourses, prerequisites):
        def backtrack(i,adjacency,flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not backtrack(j,adjacency,flags):
                    return False
            flags[i] = -1
            return True
        
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur,pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not backtrack(i,adjacency,flags):
                return False
        return True

        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            board = [[int(c) for c in s.split(",")] for s in str1.split(";")]
            numCourses = int(str2)

            res = solution.canFinish(numCourses, board)
            print(res)
        else:
            break

