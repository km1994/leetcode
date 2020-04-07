'''
    621. 任务调度器

    给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

    然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

    你需要计算完成所有任务所需要的最短时间。

    示例 ：

    输入：tasks = ["A","A","A","B","B","B"], n = 2
    输出：8
    解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.

'''
class Solution:
    def leastInterval(self, tasks, n):
        length = len(tasks)
        if length <= 1:
            return length
        
        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)
        
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        
        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length

    def leastInterval1(self, tasks, n):
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort(reverse=True)                # 降序
        print(f"count:{count}")
        max_val = count[0] - 1
        res = max_val * n                       # 空余时间
        print(f"res:{res}")
        for i in range(1, len(count)):
            if count[i] > 0:
                res -= min(max_val, count[i])   # 其余任务能安排到空余时间段里 空余时间减小
        return res + len(tasks) if res > 0 else len(tasks)

 
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            nums = str1.split(",")
            k = int(str2)
            res = solution.leastInterval(nums,k)
            print(res)
        else:
            break

