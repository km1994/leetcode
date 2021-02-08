#   337. 打家劫舍 III

## 题目描述

   
    在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

    计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

    示例 1:

    输入: [3,2,3,null,3,null,1]

        3
        / \
        2   3
        \   \ 
        3   1

    输出: 7 
    解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

## 思路介绍

### 方法一 回溯法

#### 问题解析

我们仍然是对每一项进行决策：如果我抢的话，所得到的最大价值是多少。如果我不抢的话，所得到的最大价值是多少。

#### 思路

1. 遍历二叉树，都每一个节点我们都需要判断抢还是不抢。
   1. 如果抢了的话， 那么我们不能继续抢其左右子节点
   2. 如果不抢的话，那么我们可以继续抢左右子节点，当然也可以不抢。抢不抢取决于哪个价值更大。      
2. 抢不抢取决于哪个价值更大。
   
#### 代码

```python
import sys
sys.path.append("../../topic13_tree/") # 这句是为了导入_config
from T_tree.Tree import Tree
class Solution:
    def dfs(self,root):
        if not root:
            return [0,0]
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return [max(l)+max(r),root.val+l[0]+r[0]]

    def rob(self, root):
        return max(self.dfs(root))
        
if __name__ == "__main__":
    
    tree = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            node_list = str1.split(",")
            for node in node_list:
                tree.add(int(node))

            print(f"层次遍历：{tree.traverse(tree.root)}")

            res = solution.rob(tree.root)
            print(res)
        else:
            break
    
```



#### 复杂度计算

> 时间复杂度：O(N)，其中 N 为树的节点个数。

> 空间复杂度：O(h)，其中 h 为树的高度。
