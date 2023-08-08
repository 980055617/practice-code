dic = {"I": 1, "V": 5, "X": 10,"L": 50, "C": 100, "D": 500,"M": 1000}

class Solution:
    def romanToInt(self,s:str) -> int:
        sum = 0
        index = 1000
        for key in s:
            f = dic[key]
            if index < f:
                sum -= 2*index
            sum += f
            index = f
        return sum

if __name__ == '__main__':
    s = "LVIII"
    solution = Solution()
    print(solution.romanToInt(s))