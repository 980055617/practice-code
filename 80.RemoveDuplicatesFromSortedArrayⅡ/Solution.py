class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cnt = 0
        j = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                if cnt < 1:
                    nums[j] = nums[i]
                    j += 1
                cnt += 1
            else:
                nums[j] = nums[i]
                cnt = 0
                j += 1

        return j

if __name__ == '__main__':
    nums1 = [1,1,1,2,2,3]
    solution = Solution()
    print(solution.removeDuplicates(nums1))
    print(nums1)