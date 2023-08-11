class Solution:
    def maxArea(self, height: list[int]) -> int:
        # container's left and right position
        top = 0
        bottom = len(height) -1

        maxVol = 0

        while bottom > top:
            currentVol = (bottom - top) * min(height[top],height[bottom])
            if currentVol >= maxVol:
                maxVol = currentVol

            if height[top]<height[bottom]:
                top += 1
            else:
                bottom -= 1
        return maxVol

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(height))
