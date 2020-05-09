# leetcode Study

## 项目介绍

因为目前正在 找工作需要刷题，为了方便后期学习，我将自己刷过的 题目以及对应的解法记录 于该项目中，方便后期学习，也方便大家学习，如果有帮助，麻烦给个 star , Thank you!

**本项目目前正在更新，而且我们组织了一个学习小组，如果你也面临着找工作刷题每人讨论的烦恼，可以联系我，欢迎你的加入！！！**

## 题目思维导图

1. [已完成题目思维导图](https://shimo.im/mindmaps/ckjxTq9CXyRYHgWg) 

![](img/1.png)

2. [在做题目思维导图](https://shimo.im/mindmaps/JQWpGvKwWKrWcxTw) 

![](img/2.png)


## 题目汇总

### [以前刷的题目，未加注解](old/)

![](img/3.png)

### [简单题](topic1_easy/)
1. [74. 搜索二维矩阵](topic1_easy/T74_searchMatrix/)
2. [88. 合并两个有序数组](topic1_easy/T88_merge/)
3. [136. 只出现一次的数字](topic1_easy/T136_ingleNumber/)
4. [240. 搜索二维矩阵 II](topic1_easy/T240_searchMatrix2/)
### [数组](topic2_arr/)
1. [350. 两个数组的交集 II](topic1_easy/T_select_max_min/)
2. [1. 两数之和](topic1_easy/T1_twoSum/)
3. [56. 合并区间](topic1_easy/T56_merge/)
4. [152. 乘积最大子序列](topic1_easy/T152_maxProduct/)
5. [217. 存在重复元素](topic1_easy/T217_containsDuplicate/)
6. [238. 除自身以外数组的乘积](topic1_easy/T238_productExceptSelf/)
7. [在一个未排序的整型数组中，如何找到最大和最小的数字？](topic1_easy/T268_missingNumber/)
8. [283. 移动零](topic1_easy/T283_moveZeroes/)
9. [287. 寻找重复数](topic1_easy/T287_findDuplicate/)
10. [334. 递增的三元子序列](topic1_easy/T334_increasingTriplet/)
11. [349. 两个数组的交集](topic1_easy/T349_intersection/)
12. [350. 两个数组的交集 II](topic1_easy/T350_intersect/)
13. [836. 矩形重叠](topic1_easy/T836_isRectangleOverlap/)
### [链表](topic3_List/)
**[思路汇总](topic3_List/)**
1. [在未排序链表中，怎样移除重复的节点?](topic3_List/T_removeRepeat/)
2. [在一次遍历中，怎样发现单个链表的中间元素?](topic3_List/T_selectmid/)
3. [链表实现](topic3_List/T0_ListDifine/)
4. [21. 合并两个有序链表](topic3_List/T21_mergeTwoLists/)
5. [141. 环形链表](topic3_List/T141_hasCycle/)
6. [21. 合并两个有序链表](topic3_List/T148_sortList/)
7. [160. 相交链表](topic3_List/T160_getIntersectionNode/)
8. [234. 回文链表](topic3_List/T234_isPalindrome/)
9. [328. 奇偶链表](topic3_List/T328_oddEvenList/)
10. [23. 合并K个排序链表](topic3_List/T23_mergeKLists/)
### [动态规划](topic4_dynamic_planning_study/)
**[思路汇总](topic4_dynamic_planning_study/)**
#### 只需借鉴 上一步 （定义变量类型）
##### 介绍
此类题型的特点在于，当前位置的取值，仅与前一个位置相关，与其他位置无关，所以只需定义一个变量保存前一个值即可；
##### 类型题介绍
1. [53. 最大子序和](topic4_dynamic_planning_study/T53_maxSubArray/) 【简单】
#### 需要借鉴之前步骤（定义数组类型）
##### 介绍
此类题型的特点在于，当前位置的取值，不仅与前一个位置相关，而且与其他位置相关， 所以需定义一个长度为 len+1 的向量保存之前所计算得到的值；
##### 类型题介绍
1. [300. 最长上升子序列](topic4_dynamic_planning_study/T300_lengthOfLIS/) 【中等】
2. [139. 单词拆分](topic4_dynamic_planning_study/T139_wordBreak/) 【中等】
3. [983. 最低票价](topic4_dynamic_planning_study/T983_mincostTickets/) 【中等】
#### 需要借鉴之前步骤（定义矩阵类型）
##### 介绍
此类题型的特点在于，当前位置的取值，不仅与前一个位置相关，而且与其他位置相关， 而且该问题需要 上升 到 矩阵层次上考虑，所以需定义一个矩阵保存之前所计算得到的值；
##### 类型题介绍
1. [221. 最大正方形](topic4_dynamic_planning_study/T221_maximalSquare/) 【中等】
##### 0-1 背包问题
此类题型的特点在于元素要么取，要么不取
##### 类型题介绍
1. [416. 分割等和子集](topic4_dynamic_planning_study/T416_canPartition/) 【中等】

#### 未分类
1. [在未排序链表中，怎样移除重复的节点?](topic4_dynamic_planning_study/0811_waysToChange/)
2. [牛妹的蛋糕](topic4_dynamic_planning_study/NK_cakeNumber/)
3. [887. 鸡蛋掉落](topic4_dynamic_planning_study/T887_superEggDrop/)
4. [0-1背包问题](topic4_dynamic_planning_study/T200322_bestValue/)
5. [322. 零钱兑换](topic4_dynamic_planning_study/T200322_coinChange/)
6. [面试题10- I. 斐波那契数列](topic4_dynamic_planning_study/T200322_ib_study/)
7. [62. 不同路径](topic4_dynamic_planning_study/T200323_uniquePathsWithObstacles/)
8. [63. 不同路径 II](topic4_dynamic_planning_study/T200323_uniquePaths/)
### [字符串](topic5_string/)
**[思路汇总](topic5_string/)**
1. [5. 最长回文子串](topic5_string/T5_longestPalindrome/)
2. [125. 验证回文串](topic5_string/T125_isPalindrome/)
3. [242. 有效的字母异位词](topic5_string/T242_isAnagram/)
4. [387. 字符串中的第一个唯一字符](topic5_string/T387_firstUniqChar/)
5. [466. 统计重复个数](topic5_string/T466_getMaxRepetitions/)
### [栈](topic6_stack/)
**[思路汇总](topic6_stack/)**
1. [150. 逆波兰表达式求值](topic6_stack/T387_firstUniqChar/)
### [排序](topic7_sorted/)
**[思路汇总](topic7_sorted/)**
1. [插入排序](topic7_sorted/T_insert_sorted/)
2. [快速排序](topic7_sorted/T_quick_sort/)
3. [376. 摆动序列](topic7_sorted/T376_wiggleMaxLength/)
### [二分查找](topic8_binary_search/)
**[思路汇总](topic8_binary_search/)**
1. [15. 三数之和](topic8_binary_search/T15_three_sum/)
2. [18. 四数之和](topic8_binary_search/T18_forth_sum/)
3. [33. 搜索旋转排序数组](topic8_binary_search/T33_search/)
4. [162. 寻找峰值](topic8_binary_search/T162_findPeakElement/)
5. [1095. 山脉数组中查找目标值](topic8_binary_search/T1095_findInMountainArray/)
6. [11. 盛最多水的容器](topic8_binary_search/T11_maxArea/)
7. [面试题 08.11. 硬币](topic8_binary_search/T1248_numberOfSubarrays/)
8. [神奇数字](topic8_binary_search/NK_change/) 【[牛客网](https://www.nowcoder.com/practice/01e7bedf5dd2421aa6f879fd8055e51d?tpId=110&tqId=33453&tPage=1&rp=1&ru=/ta/job-code&qru=/ta/job-code/question-ranking)】 【难度：1】
9. [69. x 的平方根](topic8_binary_search/T69_mySqrt/) 【[leetcode]](https://leetcode-cn.com/problems/sqrtx/)】 【简单】
### [哈希表](topic9_hash_table/)
**[思路汇总](topic9_hash_table/)**
1. [171. Excel表列序号](topic9_hash_table/T171_titleToNumber/)
2. [454. 四数相加 II](topic9_hash_table/T454_forth_sum/)
3. [面试题56 - I. 数组中数字出现的次数](topic1_easy/MST56_1_singleNumbers/)
4. [141. 环形链表](topic9_hash_table/T141_hasCycle/)
### [队列](topic10_queue/)
**[思路汇总](topic10_queue/)**
1. [239. 滑动窗口最大值](topic10_queue/T239_maxSlidingWindow/)
2. [347. 前 K 个高频元素](topic10_queue/T347_topKFrequent/)
3. [621. 任务调度器](topic10_queue/T621_leastInterval/)
4. [933. 最近的请求次数](topic10_queue/T933_RecentCounter/)
### [堆](topic11_heap/)
**[思路汇总](topic11_heap/)**
1. [堆排序](topic11_heap/T_HeapSort)
2. [215. 数组中的第K个最大元素](topic11_heap/T215_findKthLargest/)
3. [295. 数据流的中位数](topic11_heap/T295_MedianFinder/)
4. [378. 有序矩阵中第K小的元素](topic11_heap/T378_kthSmallest/)
### [回溯法](topic12_backtrack/)
**[思路汇总](topic12_backtrack/)**
1. [22. 括号生成](topic12_backtrack/T22_generateParenthesis/)
2. [46. 全排列](topic12_backtrack/T46_permute/)
3. [79. 单词搜索](topic12_backtrack/T79_exist/)
4. [131. 分割回文串](topic12_backtrack/T131_partition/)
5. [200. 岛屿数量](topic12_backtrack/T200_numIslands/)
6. [212. 单词搜索 II](topic12_backtrack/T212_findWords/)
7. [980. 不同路径 III](topic12_backtrack/T980_uniquePathsIII/)
8. [98. 验证二叉搜索树](topic12_backtrack/T98_isValidBST/) 【中等】
9. [140. 单词拆分 II](topic12_backtrack/T140_wordBreak/) 【困难】
### [树](topic13_tree/)
**[思路汇总](topic13_tree/)**
1. [树构建](topic13_tree/T_tree)
2. [面试题28. 对称的二叉树](topic13_tree/T28_isSymmetric/)
3. [104. 二叉树的最大深度](topic13_tree/T104_maxDepth/)
4. [110. 平衡二叉树](topic13_tree/T110_isBalanced/)
5. [111. 二叉树的最小深度](topic13_tree/T111_minDepth/)
6. [112. 路径总和](topic13_tree/T112_hasPathSum/)
7. [113. 路径总和 II](topic13_tree/T113_pathSum/)
8. [129. 求根到叶子节点数字之和](topic13_tree/T129_sumNumbers/)
9. [230. 二叉搜索树中第K小的元素](topic13_tree/T230_kthSmallest/)
10. [236. 二叉树的最近公共祖先](topic13_tree/T236_lowestCommonAncestor/)
11. [257. 二叉树的所有路径](topic13_tree/T257_binaryTreePaths/)
12. [297. 二叉树的序列化与反序列化](topic13_tree/T297_Codec/)
13. [563. 二叉树的坡度](topic13_tree/T563_findTilt/)
### [归并排序](topic15_merge/)
**[思路汇总](topic15_merge/)**
1. [面试题51. 数组中的逆序对](topic15_merge/TM51_reversePairs/)
### [快慢指针](topic16_speed_pointer/)
**[思路汇总](topic16_speed_pointer/)**
1. [202. 快乐数](topic16_speed_pointer/T202_isHappy/)
2. [283. 移动零](topic16_speed_pointer/T283_moveZeroes/) 【简单】
### [贪心算法](topic17_greedy/)
**[思路汇总](topic17_greedy/)**
1. [45. 跳跃游戏 II](topic17_greedy/T45_jump/)
### [递归](topic18_recursive/)
**[思路汇总](topic18_recursive/)**
### [分治](topic19_divide_and_conquer/)
**[思路汇总](topic19_divide_and_conquer/)**
### [分支限界法](topic20_branch_and_bound_method/)
**[思路汇总](topic20_branch_and_bound_method/)**
### [位运算](topic21_Bit_operation/)
**[思路汇总](topic21_Bit_operation/)**
1. [136. 只出现一次的数字](topic17_greedy/T136_ingleNumber/)
### [面试题](interview/)
1. [美团 2020 年春招](interview/meituan_interview/)
2. [携程 2020 年春招](interview/ctrip_interview/)

## 参考

1. [leetcode Study 网站](https://leetcode-cn.com/problemset/all/)
2. [剑指 offer](https://www.nowcoder.com/ta/coding-interviews)

