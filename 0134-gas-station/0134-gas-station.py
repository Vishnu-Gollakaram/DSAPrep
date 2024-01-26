''' # My approach 0(n^2) TLE
class Solution:
    def canReach(self, ind, arr, cost):
        start = ind
        end = start - 1
        length = len(arr)
        if end < 0:
            end = length - 1
        curReach = 0
        while ind % length != end:
            curReach += arr[ind % length] - cost[ind % length]
            if curReach <= 0:
                return False
            ind += 1
        return curReach + arr[end] - cost[end] >= 0
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        for i in range(length):
            if self.canReach(i, gas, cost):
                return i
        return -1
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start_index = i + 1

        return start_index if total_gas >= total_cost else -1
