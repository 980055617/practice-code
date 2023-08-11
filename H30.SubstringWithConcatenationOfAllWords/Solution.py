class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        l_word, n_word, answer, wordFreq= len(words[0]), len(words), [], {}
        for i in words:
            if i in wordFreq:
                wordFreq[i] += 1
            else:
                wordFreq[i] = 1

        # start searching
        for head_i in range(len(s)-l_word*n_word+1):
            check_word = {}
            for word in range(head_i,head_i+l_word*n_word,l_word):
                # add each word to dict
                if s[word:word+l_word] in check_word:
                    check_word[s[word:word+l_word]] += 1
                else:
                    check_word[s[word:word+l_word]] = 1

            # compare with origin dict
            if check_word == wordFreq:
                answer.append(head_i)

        return answer


if __name__ == '__main__':
    s = "ababaab"
    words = ["ab","ba","ba"]
    solution = Solution()
    print(solution.findSubstring(s,words))
