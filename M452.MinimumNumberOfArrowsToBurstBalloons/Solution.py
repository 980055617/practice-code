class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        startIndex, endIndex, length, ans = -1, -1, len(intervals), []

        if length == 0:
            ans.append(newInterval)
            return ans

        for i in range(length):
            if newInterval[0] <= intervals[i][1] and startIndex == -1:
                startIndex = i
            if newInterval[1] >= intervals[i][0]:
                endIndex = i
            else:
                break
        else:
            endIndex = length - 1

        if startIndex == -1:
            intervals.append(newInterval)
            return intervals

        if endIndex == -1:
            intervals.insert(0,newInterval)
            return intervals

        if endIndex < startIndex:
            intervals.insert(startIndex,newInterval)
            return intervals

        for i in range(length):
            if i < startIndex or i > endIndex:
                ans.append(intervals[i])
            elif i == startIndex:
                ans.append([min(intervals[startIndex][0],newInterval[0]),max(intervals[endIndex][1],newInterval[1])])

        return ans

if __name__ == '__main__':
    intervals = [[3,5],[12,15]]
    newInterval = [6,6]
    solution = Solution()
    print(solution.insert(intervals,newInterval))
