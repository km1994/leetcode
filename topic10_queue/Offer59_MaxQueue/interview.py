'''
    剑指 Offer 59 - II. 队列的最大值

    请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

    若队列为空，pop_front 和 max_value 需要返回 -1

    示例 1：

    输入: 
    ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
    [[],[1],[2],[],[],[]]
    输出: [null,null,null,2,1,2]
    示例 2：

    输入: 
    ["MaxQueue","pop_front","max_value"]
    [[],[],[]]
    输出: [null,-1,-1]

'''
import queue
class MaxQueue:
    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans
      
if __name__ == "__main__":
    
    solution = RecentCounter()
    while 1:
        str1 = input()
        if str1 != "":
            num1 = int(str1)
            res = solution.ping(num1)
            print(res)
        else:
            break

