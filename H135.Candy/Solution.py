class Solution:
    def candy(self, ratings: list[int]) -> int:
        length = len(ratings)
        tmp_list = [1] * length

        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                tmp_list[i] = tmp_list[i-1] + 1

        for i in range(length-2, -1, -1):
            if ratings[i] > ratings[i+1] and tmp_list[i] <= tmp_list[i+1]:
                tmp_list[i] = tmp_list[i+1] + 1
        return sum(tmp_list)

if __name__ == '__main__':
    ratings = [1,0,2]
    solution = Solution()
    print(solution.candy(ratings))
