class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2: return 0
        ans = 0
        i = 1
        j = len(height) - 1

        lmax = height[0]
        rmax = height[-1]

        while i <= j:
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]

            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1

            else:
                ans += rmax - height[j]
                j -= 1

        return ans


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap(height))
