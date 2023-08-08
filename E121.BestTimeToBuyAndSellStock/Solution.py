class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxV = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                maxV = max(maxV, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1
        return maxV

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))