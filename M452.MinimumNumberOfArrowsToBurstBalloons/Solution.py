class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points)
        ans = 1
        range = points[0][1]
        for start, end in points[1:]:
            if start <= range:
                if end < range:
                    range = end
            else:
                ans += 1
                range = end

        return ans

if __name__ == '__main__':
    points = [[10,16],[2,8],[1,6],[7,12]]
    solution = Solution()
    print(solution.findMinArrowShots(points))
