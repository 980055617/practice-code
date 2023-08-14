class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums,target))