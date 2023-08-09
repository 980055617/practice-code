class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, H = len(needle), len(haystack)
        for i in range(H-N+1):
            for j in range(N):
                if needle[j] != haystack[i + j]:
                    break
                if j == N - 1:
                    return i

        return -1
        # or just use ->
        # return haystack.find(needle)

if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    solution = Solution()
    print(solution.strStr(hasattr,needle))