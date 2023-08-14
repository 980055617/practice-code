class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        length = len(magazine)
        for key in ransomNote:
            magazine = magazine.replace(key,'',1)
        if length == len(magazine) + len(ransomNote):
            return True

if __name__ == '__main__':
    ransomNote = "a"
    magazine = "b"
    solution = Solution()
    print(solution.romanToInt(ransomNote,magazine))