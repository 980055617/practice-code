class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ansList= []
        length = len(nums)
        for i in range(length -2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = length -1
            while right > left:
                sums = nums[i] + nums[left] + nums[right]
                if sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
                else:
                    ansList.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return ansList

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    solution = Solution()
    print(solution.threeSum(nums))
