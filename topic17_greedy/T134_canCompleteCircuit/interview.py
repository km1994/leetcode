class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
            方法：贪心算法
            分析：
                if 总油量>=总消耗量，则表示 该车可以跑完全程
                if 当前 加油站的油量gas[i] > 耗油量 cost[i]
                    说明他可以作为 初始加油站 继续往下跑
                else 该加油站非 初始加油站，只能选择下一个
        '''
        # step 1：判空
        n_len = len(gas)
        if n_len<=0:
            return -1
        
        total_tank = 0      # 总剩余油量
        curr_tank = 0       # 当前油量
        start_station = 0
        for i in range(n_len):
            total_tank = total_tank+(gas[i]-cost[i])
            curr_tank = curr_tank+(gas[i]-cost[i])
            # step 2：当前节点油量不足，不能作为初始节点
            if curr_tank<0:
                curr_tank = 0
                start_station=i+1
        return start_station if total_tank>=0 else -1