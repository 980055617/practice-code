class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        # check up nums2
        for i in nums2:

            # nums1 smaller than nums2
            while nums1[j] < i and j<m:
                j += 1

            # nums1 out of range
            if j >= m:
                nums1[j] = i

            # insert nums2 between nums1
            else:
                nums1.insert(j,i)
                nums1.pop()
            j +=1
            m +=1

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution = Solution()
    solution.merge(nums1,m,nums2,n)
    print(nums1)