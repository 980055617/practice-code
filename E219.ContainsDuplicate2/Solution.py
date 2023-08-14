class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hset = {}
        for i in range(len(nums)):
            if nums[i] in hset and abs(i - hset[nums[i]]) <= k:
                return True


if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums,k))