# 117. 填充每个节点的下一个右侧节点指针 II

## 题目
### 介绍 

    给定一个二叉树

    struct Node {
        int val;
        Node *left;
        Node *right;
        Node *next;
    }
    填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

    初始状态下，所有 next 指针都被设置为 NULL。

    输入：root = [1,2,3,4,5,null,7]
    输出：[1,#,2,3,#,4,5,7,#]
    解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

## 解法

### 方法一 层次变量法 + dfs

#### 思路：

1. 定义 一个 列表存储 本层 节点；
2. 遍历 上一层节点 list:
    2.1 若 左节点 非空，则加入；
    2.2 若 右节点非空，则加入；
3. 判断 本层 节点列表 是否 大于 1：
    3.1 遍历 本层 列表，并将 每个 next 指针，让这个指针指向其下一个右侧节点；
4. 判断 nowNodeList 是否非空：
    4.1 非空，向下一层 遍历；

#### 代码
```s
   import sys
sys.path.append("..") # 这句是为了导入_config

from T_tree.Tree import Tree
import math

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
            方法：层次变量法 + dfs
            思路：
                1. 定义 一个 列表存储 本层 节点；
                2. 遍历 上一层节点 list:
                    2.1 若 左节点 非空，则加入；
                    2.2 若 右节点非空，则加入；
                3. 判断 本层 节点列表 是否 大于 1：
                    3.1 遍历 本层 列表，并将 每个 next 指针，让这个指针指向其下一个右侧节点；
                4. 判断 nowNodeList 是否非空：
                    4.1 非空，向下一层 遍历；
        '''
        if root == None:
            return
        
        def dfs(currNodeList):
            nowNodeList = []
            for currNode in currNodeList:
                if currNode.left:
                    nowNodeList.append(currNode.left)
                if currNode.right:
                    nowNodeList.append(currNode.right)
            
            if len(nowNodeList) > 1:
                for i in range(0,len(nowNodeList)-1):
                    nowNodeList[i].next = nowNodeList[i+1]
            if nowNodeList:
                dfs(nowNodeList)
        
        dfs([root])
        return root
```

##### 复杂度计算

> 时间复杂度：O(logn)

> 空间复杂度：O(n)