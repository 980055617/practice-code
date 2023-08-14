class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer = {}
        for i in strs:
            Sword = ''.join(sorted(i))
            if Sword in answer:
                answer[Sword].append(i)
            else:
                answer[Sword] = [i]
        return answer.values()

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    solution = Solution()
    print(solution.groupAnagrams(strs))
