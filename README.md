# Leetcode 刷题手册

## 目录

- [Leetcode 刷题手册](#leetcode-刷题手册)
  - [目录](#目录)
  - [项目介绍](#项目介绍)
  - [题目思维导图](#题目思维导图)
  - [题目汇总](#题目汇总)
    - [以前刷的题目，未加注解](#以前刷的题目未加注解)
    - [简单题](#简单题)
    - [数组](#数组)
    - [链表](#链表)
    - [动态规划](#动态规划)
      - [只需借鉴 上一步 （定义变量类型）](#只需借鉴-上一步-定义变量类型)
        - [介绍](#介绍)
        - [类型题介绍](#类型题介绍)
      - [需要借鉴之前步骤（定义数组类型）](#需要借鉴之前步骤定义数组类型)
        - [介绍](#介绍-1)
        - [类型题介绍](#类型题介绍-1)
      - [需要借鉴之前步骤（定义矩阵类型）](#需要借鉴之前步骤定义矩阵类型)
        - [介绍](#介绍-2)
        - [类型题介绍](#类型题介绍-2)
        - [0-1 背包问题](#0-1-背包问题)
        - [类型题介绍](#类型题介绍-3)
      - [未分类](#未分类)
    - [字符串](#字符串)
    - [栈](#栈)
    - [排序](#排序)
    - [二分查找](#二分查找)
    - [哈希表](#哈希表)
    - [队列](#队列)
    - [堆](#堆)
    - [回溯法](#回溯法)
    - [树](#树)
    - [归并排序](#归并排序)
    - [快慢指针](#快慢指针)
    - [贪心算法](#贪心算法)
    - [递归](#递归)
    - [分治](#分治)
    - [分支限界法](#分支限界法)
    - [位运算](#位运算)
    - [滑动窗口](#滑动窗口)
    - [数学题](#数学题)
    - [三指针](#三指针)
    - [左右指针](#左右指针)
    - [面试题](#面试题)
  - [参考](#参考)

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
5. [50. Pow(x, n)](topic1_easy/T50_myPow/)【[leetcode]](https://leetcode-cn.com/problems/powx-n/)】 【简单】
6. [118. 杨辉三角 I](topic1_easy/T118_generate/)【[leetcode]](https://leetcode-cn.com/problems/pascals-triangle/)】 【简单】
7. [119. 杨辉三角 II](topic1_easy/T119_getRow/)【[leetcode]](https://leetcode-cn.com/problems/pascals-triangle-ii/)】 【简单】
8. [463. 岛屿的周长](topic1_easy/T463_islandPerimeter/)【[leetcode]](https://leetcode-cn.com/problems/island-perimeter/)】 【简单】
9. [941. 有效的山脉数组](topic1_easy/T941_validMountainArray/)【[leetcode]](https://leetcode-cn.com/problems/valid-mountain-array/)】 【简单】
### [数组](topic2_arr/)
1. [350. 两个数组的交集 II](topic2_arr/T_select_max_min/)
2. [1. 两数之和](topic2_arr/T1_twoSum/)
3. [56. 合并区间](topic2_arr/T56_merge/)
4. [152. 乘积最大子序列](topic2_arr/T152_maxProduct/)
5. [217. 存在重复元素](topic2_arr/T217_containsDuplicate/)
6. [238. 除自身以外数组的乘积](topic2_arr/T238_productExceptSelf/)
7. [在一个未排序的整型数组中，如何找到最大和最小的数字？](topic2_arr/T268_missingNumber/)
8. [283. 移动零](topic2_arr/T283_moveZeroes/)
9. [287. 寻找重复数](topic2_arr/T287_findDuplicate/)
10. [334. 递增的三元子序列](topic2_arr/T334_increasingTriplet/)
11. [349. 两个数组的交集](topic2_arr/T349_intersection/)
12. [350. 两个数组的交集 II](topic2_arr/T350_intersect/)
13. [836. 矩形重叠](topic2_arr/T836_isRectangleOverlap/)
14. [118. 杨辉三角](topic2_arr/T118_generate/)
15. [119. 杨辉三角 II](topic2_arr/T119_getRow/)
16. [1431. 拥有最多糖果的孩子](topic2_arr/T1431_kidsWithCandies/) 【简单】【[leetcode](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/)】
17. [面试题29. 顺时针打印矩阵](topic2_arr/MS29_spiralOrder/) 【简单】【[leetcode](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)】
18. [14. 最长公共前缀](topic2_arr/T14_longestCommonPrefix/) 【简单】【[leetcode](https://leetcode-cn.com/problems/longest-common-prefix/)】
19. [剑指 Offer 04. 二维数组中的查找](topic2_arr/jz04_findNumberIn2DArray/) 【中等】【[leetcode](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)】
20. [228. 汇总区间](topic3_List/T228_summaryRanges/) 【简单】 【[leetcode](https://leetcode.cn/problems/summary-ranges/)】
21. [260. 只出现一次的数字 III](topic3_List/singleNumber/) 【中等】 【[leetcode](https://leetcode.cn/problems/single-number-iii/)】


T260_singleNumber
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
11. [25. K 个一组翻转链表](topic3_List/T25_reverseKGroup/)
12. [面试题 02.01. 移除重复节点](topic3_List/MS0201_removeDuplicateNodes/) 【简单】 【[leetcode](https://leetcode-cn.com/problems/remove-duplicate-node-lcci/)】
13. [92. 反转链表 II](topic3_List/T92_reverseBetween/) 【中等】 【[leetcode](https://leetcode-cn.com/problems/reverse-linked-list-ii/)】
14. [83. 删除排序链表中的重复元素](topic3_List/T83_deleteDuplicates/) 【简单】 【[leetcode](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)】
15. [24. 两两交换链表中的节点](topic3_List/T24_swapPairs/) 【简单】 【[leetcode](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)】
16. [143. 重排链表](topic3_List/T143_reorderList/) 【中等】 【[leetcode](https://leetcode-cn.com/problems/reorder-list/)】
17. [剑指 Offer 22. 链表中倒数第k个节点](topic3_List/Offer22_getKthFromEnd/) 【简单】 【[leetcode](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)】
18. [面试题 02.03. 删除中间节点](topic3_List/ms0203_deleteNode/) 【简单】 【[leetcode](https://leetcode-cn.com/problems/delete-middle-node-lcci/)】
19. [19. 删除链表的倒数第 N 个结点](topic3_List/T19_removeNthFromEnd/) 【简单】 【[leetcode](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)】
### [动态规划](topic4_dynamic_planning_study/)
**[思路汇总](topic4_dynamic_planning_study/)**
#### 只需借鉴 上一步 （定义变量类型）
##### 介绍
此类题型的特点在于，当前位置的取值，仅与前一个位置相关，与其他位置无关，所以只需定义一个变量保存前一个值即可；
##### 类型题介绍
1. [53. 最大子序和](topic4_dynamic_planning_study/T53_maxSubArray/) 【简单】
2. [198. 打家劫舍](topic4_dynamic_planning_study/T198_rob/) 【[leetcode](https://leetcode-cn.com/problems/house-robber/)】 【简单】
3. [面试题46. 把数字翻译成字符串](topic4_dynamic_planning_study/MS46_translateNum/) 【[leetcode](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)】 【中等】
4. [面试题 17.16. 按摩师](topic4_dynamic_planning_study/ms1716_massage/) 【[leetcode](https://leetcode-cn.com/problems/the-masseuse-lcci/)】 【简单】
5. [746. 使用最小花费爬楼梯](topic4_dynamic_planning_study/T746_minCostClimbingStairs/) 【[leetcode](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)】 【简单】
6. [剑指 Offer 42. 连续子数组的最大和](topic4_dynamic_planning_study/offer42_maxSubArray/) 【[leetcode](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)】 【简单】
7. [面试题 08.01. 三步问题](topic4_dynamic_planning_study/M0801_waysToStep/) 【[leetcode](https://leetcode-cn.com/problems/three-steps-problem-lcci/)】 【简单】
8. [70. 爬楼梯](topic4_dynamic_planning_study/T70_climbStairs/) 【简单】
9. [面试题 16.17. 连续数列](topic4_dynamic_planning_study/ms1617_maxSubArray/) 【简单】【[leetcode](https://leetcode-cn.com/problems/contiguous-sequence-lcci/)】
#### 需要借鉴之前步骤（定义数组类型）
##### 介绍
此类题型的特点在于，当前位置的取值，不仅与前一个位置相关，而且与其他位置相关， 所以需定义一个长度为 len+1 的向量保存之前所计算得到的值；
##### 类型题介绍
1. [300. 最长上升子序列](topic4_dynamic_planning_study/T300_lengthOfLIS/) 【中等】
2. [139. 单词拆分](topic4_dynamic_planning_study/T139_wordBreak/) 【中等】
3. [983. 最低票价](topic4_dynamic_planning_study/T983_mincostTickets/) 【中等】
4. [1024. 视频拼接](topic4_dynamic_planning_study/T1024_videoStitching/) 【中等】【[leetcode](https://leetcode-cn.com/problems/video-stitching/)】
5. [64. 最小路径和](topic4_dynamic_planning_study/T64_minPathSum/) 【中等】【[leetcode](https://leetcode-cn.com/problems/minimum-path-sum/)】
6. [279. 完全平方数](topic4_dynamic_planning_study/T279_numSquares/) 【中等】【[leetcode](https://leetcode-cn.com/problems/perfect-squares/)】
#### 需要借鉴之前步骤（定义矩阵类型）
##### 介绍
此类题型的特点在于，当前位置的取值，不仅与前一个位置相关，而且与其他位置相关， 而且该问题需要 上升 到 矩阵层次上考虑，所以需定义一个矩阵保存之前所计算得到的值；
##### 类型题介绍
1. [221. 最大正方形](topic4_dynamic_planning_study/T221_maximalSquare/) 【中等】
2. [486. 预测赢家](topic4_dynamic_planning_study/T486_PredictTheWinner/) 【中等】
3. [64. 最小路径和](topic4_dynamic_planning_study/T64_minPathSum/) 【中等】【[leetcode](https://leetcode-cn.com/problems/minimum-path-sum/)】
##### 0-1 背包问题
此类题型的特点在于元素要么取，要么不取
##### 类型题介绍
1. [416. 分割等和子集](topic4_dynamic_planning_study/T416_canPartition/) 【中等】
2. [718. 最长重复子数组](topic4_dynamic_planning_study/T718_findLength)【中等】 【[leetcode](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)】

#### 未分类
1. [在未排序链表中，怎样移除重复的节点?](topic4_dynamic_planning_study/0811_waysToChange/)
2. [牛妹的蛋糕](topic4_dynamic_planning_study/NK_cakeNumber/)
3. [887. 鸡蛋掉落](topic4_dynamic_planning_study/T887_superEggDrop/)
4. [0-1背包问题](topic4_dynamic_planning_study/T200322_bestValue/)
5. [322. 零钱兑换](topic4_dynamic_planning_study/T200322_coinChange/)
6. [面试题10- I. 斐波那契数列](topic4_dynamic_planning_study/T200322_ib_study/)
7. [62. 不同路径](topic4_dynamic_planning_study/T200323_uniquePathsWithObstacles/)
8. [63. 不同路径 II](topic4_dynamic_planning_study/T200323_uniquePaths/)
9. [837. 新21点](topic4_dynamic_planning_study/T873_new21Game/) 【中等】 【[leetcode](https://leetcode-cn.com/problems/new-21-game/)】
10. [面试题 16.11. 跳水板](topic4_dynamic_planning_study/ms1611_divingBoard/) 【简单】 【[leetcode](https://leetcode-cn.com/problems/diving-board-lcci/)】
### [字符串](topic5_string/)
**[思路汇总](topic5_string/)**
1. [5. 最长回文子串](topic5_string/T5_longestPalindrome/)
2. [125. 验证回文串](topic5_string/T125_isPalindrome/)
3. [242. 有效的字母异位词](topic5_string/T242_isAnagram/)
4. [387. 字符串中的第一个唯一字符](topic5_string/T387_firstUniqChar/)
5. [466. 统计重复个数](topic5_string/T466_getMaxRepetitions/)
6. [1371. 每个元音包含偶数次的最长子字符串](topic5_string/T1371_findTheLongestSubstring/)
7. [3. 无重复字符的最长子串](topic5_string/T3_lengthOfLongestSubstring/)
8. [面试题 16.18. 模式匹配](topic5_string/MS1618_patternMatching/) 【中等】 【[leetcode](https://leetcode-cn.com/problems/pattern-matching-lcci/)】
9. [459. 重复的子字符串](topic5_string/T459_repeatedSubstringPattern/) 【中等】 【[leetcode](https://leetcode-cn.com/problems/repeated-substring-pattern/)】
10. [214. 最短回文串](topic5_string/T214_shortestPalindrome/) 【困难】 【[leetcode](https://leetcode-cn.com/problems/shortest-palindrome/)】
11. [93. 复原IP地址](topic5_string/T93_restoreIpAddresses/) 【[leetcode](https://leetcode-cn.com/problems/restore-ip-addresses/)】【中等】
12. [1002. 查找常用字符](topic5_string/T1002_commonChars/) 【[leetcode](https://leetcode-cn.com/problems/find-common-characters/)】 【简单】
### [栈](topic6_stack/)
**[思路汇总](topic6_stack/)**
1. [150. 逆波兰表达式求值](topic6_stack/T387_firstUniqChar/)
2. [155. 最小栈](topic6_stack/T155_MinStack/)
3. [394. 字符串解码](topic6_stack/T394_decodeString/) 【[leetcode](https://leetcode-cn.com/problems/decode-string/)】【中等】
4. [394. 字符串解码](topic6_stack/T84_ilargestRectangleArea/) 【[leetcode](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)】【中等】
5. [739. 每日温度](topic6_stack/T739_dailyTemperatures/)【[leetcode](https://leetcode-cn.com/problems/daily-temperatures/)】【中等】
6. [85. 最大矩形](topic6_stack/T85_maximalRectangle/)【[leetcode](https://leetcode-cn.com/problems/maximal-rectangle/)】【困难】
7.  [841. 钥匙和房间](topic6_stack/T841_canVisitAllRooms/)【[leetcode](https://leetcode-cn.com/problems/keys-and-rooms/)】【困难】
### [排序](topic7_sorted/)
**[思路汇总](topic7_sorted/)**
1. [插入排序](topic7_sorted/T_insert_sorted/)
2. [快速排序](topic7_sorted/T_quick_sort/)
3. [376. 摆动序列](topic7_sorted/T376_wiggleMaxLength/)
4. [剑指 Offer 45. 把数组排成最小的数](topic7_sorted/jz45_minNumber/) 【中等】[leetcode](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)
5. [75. 颜色分类](topic7_sorted/T75_sortColors/) 【中等】[leetcode](https://leetcode-cn.com/problems/sort-colors/)
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
9. [69. x 的平方根](topic8_binary_search/T69_mySqrt/) 【[leetcode]](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)】 【困难】
10. [4. 寻找两个正序数组的中位数](topic8_binary_search/T4_findMedianSortedArrays/) 【[leetcode]](https://leetcode-cn.com/problems/sqrtx/)】 【简单】
11. [1300. 转变数组后最接近目标值的数组和](topic8_binary_search/T1300_findBestValue/) 【[leetcode]](https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/)】 【中等】
12. [315. 计算右侧小于当前元素的个数](topic8_binary_search/T315_countSmaller/) 【[leetcode]](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)】 【困难】
13. [35. 搜索插入位置](topic8_binary_search/T35_searchInsert/) 【[leetcode]](https://leetcode-cn.com/problems/search-insert-position/)】 【简单】
14. [167. 两数之和 II - 输入有序数组](topic8_binary_search/T167_twoSum/) 【[leetcode]](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)】 【简单】
15. [392. 判断子序列](topic8_binary_search/T392_isSubsequence/) 【[leetcode]](https://leetcode-cn.com/problems/is-subsequence/)】 【简单】
16. [75. 颜色分类](topic8_binary_search/T75_sortColors/)【[leetcode]](https://leetcode-cn.com/problems/sort-colors/)】 【中等】
17.  [977. 有序数组的平方](topic8_binary_search/T997_sortedSquares/)【[leetcode]](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)】 【简单】
18.  [925. 长按键入](topic8_binary_search/T925_isLongPressedName/)【[leetcode]](https://leetcode-cn.com/problems/long-pressed-name/)】 【简单】
19.  [剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](topic8_binary_search/Offer21_exchange/)【[leetcode]](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)】 【简单】
### [哈希表](topic9_hash_table/)
**[思路汇总](topic9_hash_table/)**
1. [171. Excel表列序号](topic9_hash_table/T171_titleToNumber/)
2. [454. 四数相加 II](topic9_hash_table/T454_forth_sum/)
3. [面试题56 - I. 数组中数字出现的次数](topic1_easy/MST56_1_singleNumbers/)
4. [141. 环形链表](topic9_hash_table/T141_hasCycle/)
5. [560. 和为K的子数组](topic9_hash_table/T560_subarraySum/)
6. [1. 两数之和](topic9_hash_table/T1_twoSum/)
7. [1010. 总持续时间可被 60 整除的歌曲](topic9_hash_table/T1010_numPairsDivisibleBy60/) 【[leetcode](https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/submissions/)】【简单】
8. [41. 缺失的第一个正数](topic9_hash_table/T41_firstMissingPositive/)【[leetcode](https://leetcode-cn.com/problems/first-missing-positive/)】【困难】
9. [350. 两个数组的交集 II](topic9_hash_table/T350_intersect/)【[leetcode](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)】【简单】
10. [137. 只出现一次的数字 II](topic9_hash_table/T137_singleNumber/)【[leetcode](https://leetcode-cn.com/problems/single-number-ii/)】【中等】
11. [75. 颜色分类](topic9_hash_table/T75_sortColors/)【[leetcode]](https://leetcode-cn.com/problems/sort-colors/)】 【中等】
12. [229. 求众数 II](topic9_hash_table/T229_majorityElement/)【[leetcode]](https://leetcode-cn.com/problems/majority-element-ii/)】 【中等】
13. [771. 宝石与石头](topic9_hash_table/T771_numJewelsInStones/)【[leetcode]](https://leetcode-cn.com/problems/jewels-and-stones/)】 【简单】
14. [1365. 有多少小于当前数字的数字](topic9_hash_table/T1365_smallerNumbersThanCurrent/)【[leetcode]][(https://leetcode-cn.com/problems/jewels-and-stones](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/)/)】 【简单】
15. [973. 最接近原点的 K 个点](topic9_hash_table/T973_kClosest/)【[leetcode]][(https://leetcode-cn.com/problems/jewels-and-stones](https://leetcode-cn.com/problems/k-closest-points-to-origin/)/)】 【中等】
### [队列](topic10_queue/)
**[思路汇总](topic10_queue/)**
1. [239. 滑动窗口最大值](topic10_queue/T239_maxSlidingWindow/)
2. [347. 前 K 个高频元素](topic10_queue/T347_topKFrequent/)
3. [621. 任务调度器](topic10_queue/T621_leastInterval/)
4. [933. 最近的请求次数](topic10_queue/T933_RecentCounter/)
5. [剑指 Offer 59 - II. 队列的最大值](topic10_queue/Offer59_MaxQueue/) 【中等】【[剑指 Offer](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)】
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
10. [210. 课程表 II](topic12_backtrack/T210_findOrder/) 【[leetcode](https://leetcode-cn.com/problems/course-schedule-ii/)】【中等】
11. [1028. 从先序遍历还原二叉树](topic12_backtrack/T1028_recoverFromPreorder/) 【[leetcode](https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/)】【困难】
12. [337. 打家劫舍 III](topic12_backtrack/T337_rob/) 【[leetcode](https://leetcode-cn.com/problems/house-robber-iii/)】【中等】
13. [332. 重新安排行程](topic12_backtrack/T332_findItinerary/) 【[leetcode](https://leetcode-cn.com/problems/reconstruct-itinerary/)】【中等】
14. [216. 组合总和 III](topic12_backtrack/T216_combinationSum3/) 【[leetcode](https://leetcode-cn.com/problems/combination-sum-iii/)】【中等】
15. [37. 解数独](topic12_backtrack/T37_solveSudoku/) 【[leetcode](https://leetcode-cn.com/problems/sudoku-solver/)】【困难】
16. [93. 复原IP地址](topic12_backtrack/T93_restoreIpAddresses/) 【[leetcode](https://leetcode-cn.com/problems/restore-ip-addresses/)】【中等】
17. [40. 组合总和 II](topic12_backtrack/T40_combinationSum2/) 【[leetcode](https://leetcode-cn.com/problems/combination-sum-ii/)】【中等】
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
14. [100. 相同的树](topic13_tree/T100_isSameTree/)【简单】 【[leetcode](https://leetcode-cn.com/problems/same-tree/)】
15. [114. 二叉树展开为链表](topic13_tree/T114_flatten/)【中等】 【[leetcode](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)】
16. [107. 二叉树的层次遍历 II](topic13_tree/T107_levelOrderBottom) 【[简单](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)】
17. [94. 二叉树的中序遍历](topic13_tree/T94_inorderTraversal) 【[简单](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)】
18. [404. 左叶子之和](topic13_tree/T404_sumOfLeftLeaves) 【[简单](https://leetcode-cn.com/problems/sum-of-left-leaves/)】
19. [剑指 Offer 07. 重建二叉树](topic13_tree/offer07_buildTree) 【[中等](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)】
20. [700. 二叉搜索树中的搜索](topic13_tree/T700_searchBST) 【[简单](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/)】
### [归并排序](topic15_merge/)
**[思路汇总](topic15_merge/)**
1. [面试题51. 数组中的逆序对](topic15_merge/TM51_reversePairs/)
### [快慢指针](topic16_speed_pointer/)
**[思路汇总](topic16_speed_pointer/)**
1. [202. 快乐数](topic16_speed_pointer/T202_isHappy/)
2. [283. 移动零](topic16_speed_pointer/T283_moveZeroes/) 【简单】
3. [109. 有序链表转换二叉搜索树](topic16_speed_pointer/T109_sortedListToBST/)【[leetcode]](https://leetcode-cn.com/problems/sort-colors/)】 【中等】
4. [763. 划分字母区间](topic16_speed_pointer/T763_partitionLabels/)【[leetcode](https://leetcode-cn.com/problems/partition-labels/)】【中等】
5. [剑指 Offer 22. 链表中倒数第k个节点](topic16_speed_pointer/Offer22_getKthFromEnd/) 【简单】 【[leetcode](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)】
6. [287. 寻找重复数](topic16_speed_pointer/T287_findDuplicate/) 【中等】 【[leetcode](https://leetcode-cn.com/problems/find-the-duplicate-number/)】
### [贪心算法](topic17_greedy/)
**[思路汇总](topic17_greedy/)**
1. [1221. 分割平衡字符串](topic17_greedy/T1221_balancedStringSplit/)【[leetcode](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/)】【简单】
2. [45. 跳跃游戏 II](topic17_greedy/T45_jump/)
3. [680. 验证回文字符串 Ⅱ](topic17_greedy/T680_validPalindrome/)
4. [763. 划分字母区间](topic17_greedy/T763_partitionLabels/)【[leetcode](https://leetcode-cn.com/problems/partition-labels/)】
5. [406. 根据身高重建队列](topic17_greedy/T406_reconstructQueue/)【[leetcode](https://leetcode-cn.com/problems/queue-reconstruction-by-height/)】【中等】
6. [134. 加油站](topic17_greedy/T134_canCompleteCircuit/)【[leetcode](https://leetcode-cn.com/problems/gas-station/)】【中等】
7.  [135. 分发糖果](topic17_greedy/T134_canCompleteCircuit/)【[leetcode](https://leetcode-cn.com/problems/candy/)】【困难】
### [递归](topic18_recursive/)
**[思路汇总](topic18_recursive/)**
### [分治](topic19_divide_and_conquer/)
**[思路汇总](topic19_divide_and_conquer/)**
### [分支限界法](topic20_branch_and_bound_method/)
**[思路汇总](topic20_branch_and_bound_method/)**
1. [210. 课程表 II](topic12_backtrack/T210_findOrder/) 【[leetcode](https://leetcode-cn.com/problems/course-schedule-ii/)】【中等】
2. [126. 单词接龙 II](topic12_backtrack/T126_ffindLadders/) 【[leetcode](https://leetcode-cn.com/problems/word-ladder-ii/submissions/)】【困难】
3. [127. 单词接龙 I](topic12_backtrack/T127_ladderLength/) 【[leetcode](https://leetcode-cn.com/problems/word-ladder-ii/submissions/)】【中等】
4. [剑指 Offer 32 - II. 从上到下打印二叉树 II](topic12_backtrack/Offer32_levelOrder/) 【[leetcode](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)】【简单】
5.  [199. 二叉树的右视图](topic12_backtrack/T199_rightSideView/) 【[leetcode](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)】【简单】
6.   [513. 找树左下角的值](topic12_backtrack/T513_findBottomLeftValue/) 【[leetcode](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)】【简单】
### [位运算](topic21_Bit_operation/)
**[思路汇总](topic21_Bit_operation/)**
1. [136. 只出现一次的数字](topic21_Bit_operation/T136_ingleNumber/)
2. [201. 数字范围按位与](topic21_Bit_operation/T201_rangeBitwiseAnd/)
### [滑动窗口](topic22_move_window/)
**[思路汇总](topic22_move_window/)**
1. [76. 最小覆盖子串](topic22_move_window/T76_minWindow/)
2. [219. 存在重复元素 II](topic22_move_window/T219_containsNearbyDuplicate/) 【[leetcode](https://leetcode-cn.com/problems/contains-duplicate-ii/)】 【简单】
3. [209. 长度最小的子数组](topic22_move_window/T209_minSubArrayLen/) 
4. [1343. 大小为 K 且平均值大于等于阈值的子数组数目](topic22_move_window/T1343_numOfSubarrays/) 
5. [1052. 爱生气的书店老板](topic22_move_window/T1052_maxSatisfied/) 
### [数学题](topic23_math/)
**[思路汇总](topic23_math/)**
1. [976. 三角形的最大周长](topic23_math/T976_largestPerimeter/) 【简单】
2. [990. 等式方程的可满足性](topic23_math/T990_UnionFind/) 【中等】
3. [9. 回文数](topic23_math/T9_isPalindrome/) 【中等】
4. [67. 二进制求和](topic23_math/T67_addBinary/) 【[leetcode](https://leetcode-cn.com/problems/add-binary/)】 【简单】
5. [73. 矩阵置零](topic23_math/T73_setZeroes/) 【[leetcode](https://leetcode-cn.com/problems/set-matrix-zeroes/)】 【简单】
6. [31. 下一个排列](topic23_math/T31_nextPermutation/) 【[leetcode](https://leetcode-cn.com/problems/next-permutation/)】 【中等】
7. [LCP 17. 速算机器人](topic23_math/LCP17_calculate/) 【[leetcode](https://leetcode-cn.com/problems/nGK0Fy/)】 【简单】
### [三指针](topic24_three_pointer/)
1. [75. 颜色分类](topic7_sorted/T75_sortColors/) 【中等】[leetcode](https://leetcode-cn.com/problems/sort-colors/)
### [左右指针](topic25_left_right_pointer/)
2. [面试题 16.16. 部分排序](topic25_left_right_pointer/MS1616_subSort1/) 【中等】[leetcode](https://leetcode-cn.com/problems/sub-sort-lcci/)
### [面试题](interview/)
1. [美团 2020 年春招](interview/meituan_interview/)
2. [携程 2020 年春招](interview/ctrip_interview/)

## 参考

1. [leetcode Study 网站](https://leetcode-cn.com/problemset/all/)
2. [剑指 offer](https://www.nowcoder.com/ta/coding-interviews)

