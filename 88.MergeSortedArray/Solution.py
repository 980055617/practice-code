class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        cnt =0
        j = 0
        for i in range(len(nums)):
            # replace num to 0 when same as val
            if nums[j] == val:
                nums.pop(j)
                nums.append(0)
                j -= 1
                cnt+=1
            j +=1
        k = len(nums) -cnt
        return k


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    solution = Solution()
    solution.removeElement(nums,val)
    print(nums)