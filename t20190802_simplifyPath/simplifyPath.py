#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: generateMatrix.py
@time: 2019/7/24
@rel： https://leetcode-cn.com/problems/spiral-matrix-ii/
@url：
@desc:
    71. 简化路径

    以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

    示例 1：
        输入："/home/"
        输出："/home"
        解释：注意，最后一个目录名后面没有斜杠。
    示例 2：
        输入："/../"
        输出："/"
        解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
    示例 3：
        输入："/home//foo/"
        输出："/home/foo"
        解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
    示例 4：
        输入："/a/./b/../../c/"
        输出："/c"
    示例 5：
        输入："/a/../../b/../c//.//"
        输出："/c"
    示例 6：
        输入："/a//b////c/d//././/.."
        输出："/a/b/c"

'''
class Solution:
    def __init__(self):
        pass

    # 自底向上
    def simplifyPath(self, path):
        path_stack = []

        if not path:
            return ''

        if len(path) == 1:
            return '/'

        now_path = ''
        if path[-1] is not '/':
            path = path +'/'

        for i in range(1,len(path)):
            # print("path[{0}]={1}".format(i,path[i]))
            if path[i] is not '/':
                now_path = now_path + path[i]
            else:
                if now_path == '.':
                    now_path = ''
                    continue
                elif now_path == '..':
                    if len(path_stack) > 0:
                        # print("path_stack:{0}".format(path_stack))
                        path_stack.pop()
                elif len(now_path):
                    path_stack.append(now_path)
                now_path =''

        return '/'+'/'.join(path_stack)


if __name__ == "__main__":

    solution = Solution()

    path = "/home/"
    res1 = solution.simplifyPath(path)
    print("res1:{0}".format(res1))

    path = "/../"
    res1 = solution.simplifyPath(path)
    print("res2:{0}".format(res1))
    #
    path = "/home//foo/"
    res1 = solution.simplifyPath(path)
    print("res1:{0}".format(res1))
    #
    path = "/a/./b/../../c/"
    res1 = solution.simplifyPath(path)
    print("res1:{0}".format(res1))
    #
    path = "/a/../../b/../c//.//"
    res1 = solution.simplifyPath(path)
    print("res2:{0}".format(res1))

    path = "/a//b////c/d//././/.."
    res1 = solution.simplifyPath(path)
    print("res1:{0}".format(res1))


