class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 0
        valueCnt = 0
        while right < len(prices) - 1:

            while prices[left] > prices[left + 1]:
                if right >= len(prices) - 2:
                    break
                left += 1
                right += 1

            if prices[right] > prices[right + 1]:
                valueCnt += prices[right] - prices[left]
                left = right + 1
            right += 1

        valueCnt += prices[right] - prices[left]
        return valueCnt

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))
