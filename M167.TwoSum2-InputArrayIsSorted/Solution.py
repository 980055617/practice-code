class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        bottom = len(numbers)-1
        top = 0
        while True:
            value = numbers[top] + numbers[bottom]
            if value == target:
                return [top + 1,bottom + 1]
            elif value > target:
                bottom -= 1
            else:
                top += 1

if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(numbers,target))
