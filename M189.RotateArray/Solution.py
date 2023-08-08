class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            pass
        else:
            length =len(nums)
            k = k % length
            list = nums[-k:]
            list1 = list + nums[:length-k]
            nums.clear()
            nums.extend(list1)
            #print(nums)

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution = Solution()
    solution.rotate(nums,k)
    print(nums)