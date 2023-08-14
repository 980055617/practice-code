from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s,t))