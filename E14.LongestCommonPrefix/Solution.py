class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans= ""
        strs = sorted(strs)
        print(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans += first[i]
        return ans

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))