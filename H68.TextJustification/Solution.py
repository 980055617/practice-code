class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans, cash,tmp, length = [], [], "", maxWidth
        for i in words:
            if length - len(i) < 0:
                length += 1
                space = len(cash)-1
                if space != 0:
                    more_space = length // (space)
                    not_evenly = length % (space)
                    for j in cash[:-1]:
                        tmp += j + ' '*(more_space+1)
                        if not_evenly >0:
                            tmp += ' '
                            not_evenly -= 1
                    tmp += cash[-1]
                    ans.append(tmp)
                else:
                    tmp += cash[-1]
                    tmp += ' '*length
                    ans.append(tmp)
                length = maxWidth
                cash = []
                tmp = ""

            length -= len(i) + 1
            cash.append(i)
        for i in cash:
            tmp += i + ' '
        tmp += ' '*(length)
        if length < 0:
            ans.append(tmp[:-1])
        else:
            ans.append(tmp)
        return ans


if __name__ == '__main__':
    words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
    maxWidth = 16
    solution = Solution()
    print(solution.fullJustify(words,maxWidth))
