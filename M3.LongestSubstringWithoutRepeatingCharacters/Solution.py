class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        str1 = ''
        for i in s:
            if i in str1:
                index = str1.find(i)
                str1 = str1[index+1:]
            str1 += i
            answer = max(answer, len(str1))
        return answer

if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))

