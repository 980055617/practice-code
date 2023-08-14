from itertools import zip_longest
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))

if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    solution = Solution()
    print(solution.wordPattern(pattern,s))