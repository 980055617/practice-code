class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        if sum(gas) < sum(cost): return -1

        tank = idx = 0

        for i in range(len(gas)):

            tank+= gas[i]-cost[i]
            if tank < 0: tank, idx = 0, i+1

        return idx

if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    solution = Solution()
    print(solution.productExceptSelf(gas,cost))