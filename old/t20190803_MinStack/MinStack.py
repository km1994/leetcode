#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: MinStack.py
@time: 2019/8/03
@rel： https://leetcode-cn.com/problems/min-stack/
@url：
@desc:
    155. 最小栈

    设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。
    示例:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.

'''


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list = []
        self.min_list=[]
        self.stack_len = 0
        self.min_list_len =0

    def push(self, x):
        self.stack_list.append(x)
        self.stack_len = self.stack_len + 1
        if self.min_list_len == 0 or self.min_list[-1] >= x:
            self.min_list.append(x)
            self.min_list_len = self.min_list_len + 1

    def pop(self):
        top = self.stack_list.pop()
        if self.min_list_len > 0 and top == self.min_list[-1]:
            self.min_list.pop()
            self.min_list_len = self.min_list_len - 1

        return top

    def top(self):
        if self.stack_len >= 0:
            return self.stack_list[-1]

    def getMin(self):
        if self.min_list_len > 0:
            return self.min_list[-1]

if __name__ == "__main__":

    obj = MinStack()

    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print("obj.getMin():{0}".format(obj.getMin()))
    obj.pop()
    print("obj.top():{0}".format(obj.top()))
    print("obj.getMin():{0}".format(obj.getMin()))

