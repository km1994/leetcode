#  295. 数据流的中位数

## 题目描述

	中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

	例如，

	[2,3,4] 的中位数是 3

	[2,3] 的中位数是 (2 + 3) / 2 = 2.5

	设计一个支持以下两种操作的数据结构：

	void addNum(int num) - 从数据流中添加一个整数到数据结构中。
	double findMedian() - 返回目前所有元素的中位数。


## 示例:
```
  	addNum(1)
	addNum(2)
	findMedian() -> 1.5
	addNum(3) 
	findMedian() -> 2
```

## 思路介绍

### 方法一 堆排序法

#### 基本介绍

#### 思路

1. 对数组进行堆排序
2. 然后选取中位数
 
#### 复杂度计算

> 时间复杂度：O(nlogn) 

> 空间复杂度：O(1)

### 方法二 优先队列法

#### 基本介绍

#### 思路

1. 将中位数左边的数保存在大顶堆中，右边的数保存在小顶堆中。这样我们可以在 O(1) 时间内得到中位数。
 
#### 复杂度计算

> 时间复杂度：O(nlogn) 

> 空间复杂度：O(1)

## 参考资料

1. [图解 排序+二分查找+优先队列](https://leetcode-cn.com/problems/find-median-from-data-stream/solution/tu-jie-pai-xu-er-fen-cha-zhao-you-xian-dui-lie-by-/)