class Solution:
    def jump(self, nums: list[int]) -> int:
        # Get the length of the array
        length = len(nums)
        maxReached = 0
        reached = 0
        jumpCnt = 0
        index = 0
        # Loop to search the best jump time
        while maxReached < length -1:
            for i in range(index,maxReached+1):
                tmp = nums[i] + i
                if tmp > reached:
                    reached = tmp
                    tmp_index = i
            jumpCnt += 1
            maxReached = reached
            index = tmp_index
        return jumpCnt

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    solution = Solution()
    print(solution.jump(nums))
