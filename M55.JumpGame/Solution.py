class Solution:
    def canJump(self, nums: list[int]) -> bool:
        length = len(nums)
        max_reached = 0
        for i in range(length):
            if i > max_reached:
                return False
            reached = i + nums[i]
            if max_reached < reached:
                max_reached = reached
            if max_reached >= length - 1:
                return True

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    solution = Solution()
    print(solution.canJump(nums))
