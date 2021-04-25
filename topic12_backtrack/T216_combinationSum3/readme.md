#   216. 组合总和 III

## 题目描述

    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

    说明：

    所有数字都是正整数。
    解集不能包含重复的组合。 
    示例 1:

    输入: k = 3, n = 7
    输出: [[1,2,4]]
    示例 2:

    输入: k = 3, n = 9
    输出: [[1,2,6], [1,3,5], [2,3,4]]

## 思路介绍

### 方法一 回溯法

#### 思路

1. 回溯：dfs(k,target,index,path,res) 
   -  k：路径长度
   -  target：当前目标值
   -  index：当前索引，也就是下标位置；
   -  path：当前路径
   -  res：历史路径保存
   1. 因为组合中只允许含有 1 - 9 的正整数，所以 需要 判断 index<10;
   2.  当 当前目标值=1，当前路径不在历史路径，且当前路径的长度等于 k 时，将新路径加到 res 中；
   3.  index -> 10 循环：
       1. new_target = target - i
       2. 若 new_target>=0 且 len(path) < k:
          1. 继续回溯

#### 代码

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
            方法：回溯法
        '''
        res = []
        self.dfs(k,n,1,[],res)
        return res

    def dfs(self,k,target,begin,path,res):
        # step 1：剪枝，值 超过 [1,9]
        if begin>10:
            return 
        # step 2：满足要求
        if target==0 and len(path)==k:
            res.append(path[:])
            return 
        for index in range(begin,10):
            if target>=index and len(path)<k:
                self.dfs(k,target-index,index+1,path+[index],res)


    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        def dfs(k,target,index,path,res):
            if index > 10:
                return
            if target == 0 and path not in res and len(path)==k:
                res.append(path[:])
                return
            for i in range(index,10):
                new_target = target - i
                if new_target >= 0 and len(path) < k:
                    dfs(k,new_target,i+1,path+[i],res)

        res = []
        dfs(k,n,1,[],res)
        return res

    
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            n = int(str1)
            k = int(str2)
            print(f"n:{n}")
            print(f"k:{k}")

            res = solution.combinationSum3(k,n)
            print(res)
        else:
            break
```

#### 复杂度计算

> 时间复杂度：
> 
> 空间复杂度：


