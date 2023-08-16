class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        List = []
        char = str(nums[0])
        tmp = nums[0]

        for i in nums[1:]:
            if tmp + 1 == i:
                tmp = i
                continue
            else:
                if char != str(tmp):
                    char += '->'
                    char += str(tmp)
                List.append(char)
                tmp = i
                char = str(tmp)
        else:
            if char != str(tmp):
                char += '->'
                char += str(tmp)
            List.append(char)

        return List


if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    solution = Solution()
    solution.summaryRanges(nums)
