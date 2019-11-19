'''
    134. 加油站
'''
class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def canCompleteCircuit(self, gas, cost):
        n_len = len(gas)
        total_tank = 0
        curr_tank = 0
        start_station = 0
        for i in range(n_len):
            total_tank = total_tank + (gas[i]-cost[i])
            curr_tank = curr_tank + (gas[i]-cost[i])
            if curr_tank < 0:
                curr_tank = 0
                start_station = i + 1
        
        return start_station if total_tank >= 0 else -1

if __name__ == "__main__":

    solution = Solution()
    print("---------------1----------------")
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    res = solution.canCompleteCircuit(gas,cost)
    print("res:{0}".format(res))



        


  