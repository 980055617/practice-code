class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0 :
            return 0
        nums = sorted(list(set(nums)))
        max_cnt = 1
        cnt = 1
        tmp = nums[0]
        for i in nums[1:]:
            if i == tmp + 1:
                cnt += 1
                tmp += 1
            else:
                tmp = i
                max_cnt = max(max_cnt,cnt)
                cnt = 1
        else:
            max_cnt = max(max_cnt,cnt)
        return max_cnt

if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    solution = Solution()
    print(solution.longestConsecutive(nums))
