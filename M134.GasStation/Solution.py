class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        length = len(gas)
        tmpIndex = 0
        tmpTank = 0
        cnt = 0
        AllDiff = 0
        sum = 0
        while gas[cnt] - cost[cnt] <= 0:
            AllDiff += gas[cnt] - cost[cnt]
            cnt += 1
            if cnt >= length and AllDiff < 0:
                return -1
            elif cnt >= length:
                return 0
        tmpTank = gas[cnt] - cost[cnt]
        tmpIndex = cnt
        for i in range(cnt+1,length):
            tmp = gas[i]-cost[i]
            if  tmp > 0:
                sum += tmpTank
                if sum >= 0:
                    tmpTank = sum + tmp
                else:
                    tmpIndex = i
                    tmpTank = tmp
                    AllDiff += sum
                sum = 0
            else:
                sum += tmp
        if tmpTank + sum + AllDiff >= 0:
            return tmpIndex
        else:
            return -1

if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    solution = Solution()
    print(solution.productExceptSelf(gas,cost))
