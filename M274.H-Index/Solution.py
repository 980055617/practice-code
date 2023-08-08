class Solution:
    def hIndex(self, citations: list[int]) -> int:
        sortedCitations = sorted(citations,reverse=True)
        length = len(sortedCitations)
        for i in range(length):
            if sortedCitations[i] < i+1:
                return i
        return length

if __name__ == '__main__':
    citations = [3,0,6,1,5]
    solution = Solution()
    print(solution.hIndex(citations))
