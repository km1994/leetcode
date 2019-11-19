#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/10/13
@url：https://www.cnblogs.com/lightwindy/p/8636516.html
@desc:
    
    第 261 号问题：以图判树

    给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

    示例 1：

    输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
    输出: true
    示例 2:

    输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    输出: false
    注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edges 中。

'''
import collections
class Solution(object):
    def validTree(self, n, edges):
        lookup = collections.defaultdict(list)
        for edge in edges:
            lookup[edge[0]].append(edge[1])
            lookup[edge[1]].append(edge[0])
        visited = [False] * n

        print("lookup:{0}".format(lookup))
 
        if not self.helper(0, -1, lookup, visited):
            return False
 
        for v in visited:
            if not v:
                return False
 
        return True
 
    def helper(self, curr, parent, lookup, visited):
        print(curr, visited)
        if visited[curr]:
            return False
        visited[curr] = True
        for i in lookup[curr]:
            if (i != parent and not self.helper(i, curr, lookup, visited)):
                return False
 
        return True
 
if __name__ == '__main__':
    print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))