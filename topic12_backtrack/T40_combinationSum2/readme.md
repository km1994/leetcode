#  40. 组合总和 II

## 题目描述

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]


## 思路介绍

### 方法一 回溯法

#### 基本介绍


#### 思路


#### 代码

```s
class Solution(object):
    def combinationSum2(self, candidates, target):
        # step 1：判空
        candidates_len = len(candidates)
        if candidates_len == 0:
            return []
        # step 2：排序
        candidates.sort()
        res = []
        # step 3：回溯
        self.dfs(candidates,0, [], target,candidates_len,res)
        return res

    def dfs(self,candidates, begin, path, residue,candidates_len, res):
        '''
            方法：回溯法
            input：
                candidates          List          候选列表
                begin               int            开始位置
                path                List           当前路径
                residue             int            当前目标值
                candidates_len      int            候选列表长度            
                res                  List[]        结果列表 
            return:

        '''
        # step 1：当前目标值为零，即找到一组解
        if residue == 0:
            res.append(path[:])
            return

        for index in range(begin, candidates_len):
            # step 2：剪枝 1 当前值 超过目标值，即后面无可行解
            if candidates[index] > residue:
                break
            # step 3：剪枝 2 遇到重复值
            if index > begin and candidates[index - 1] == candidates[index]:
                continue

            path.append(candidates[index])
            self.dfs(candidates, index + 1, path, residue - candidates[index],candidates_len,res)
            path.pop()


```

   
#### 复杂度计算


