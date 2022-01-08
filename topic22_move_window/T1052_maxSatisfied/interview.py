class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        方法：滑动窗口
        解析：
            最小收益：不适用技巧下的收益；
            最大收益：最小收益+ 使用技巧下不生气所获得的最大收益
            所以这道题 核心就是 计算 使用技巧 所获得的 最大收益，因此可以转化为 滑动窗口问题
        """
        customers_len = len(customers)
        # step 1：计算最小收益：不适用技巧下的收益
        total = sum(c for c,g in zip(customers,grumpy) if g==0)
        # step 2：初始化滑动窗口，也就是 滑动窗口 取 前minutes和
        max_increase = increase = sum(c*g for c,g in zip(customers[:minutes],grumpy[:minutes]))
        # step 3：移动滑动窗口，以获得最大收益
        for i in range(minutes,customers_len):
            increase = increase+ customers[i]*grumpy[i]-customers[i-minutes]*grumpy[i-minutes]
            max_increase = max(max_increase,increase)
        return total+max_increase
