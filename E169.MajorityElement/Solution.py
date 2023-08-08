class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()

        return nums[len(nums)//2]

if __name__ == '__main__':
    nums = [3,2,3]
    solution = Solution()
    print(solution.majorityElement(nums))

"""
The intuition behind this approach is that
if an element occurs more than n/2 times in the array
(where n is the size of the array),
it will always occupy the middle position when the array is sorted.
Therefore, we can sort the array and return the element at index n/2.
"""