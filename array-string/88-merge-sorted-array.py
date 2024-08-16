class Solution:
    #  def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted_array = []
        index_1 = 0
        index_2 = 0
        while (index_1 + index_2 < m + n):
            if index_1 == m:
                sorted_array.append(nums2[index_2])
                index_2 += 1
            elif index_2 == n:
                sorted_array.append(nums1[index_1])
                index_1 += 1
            elif (nums1[index_1] <= nums2[index_2]):
                sorted_array.append(nums1[index_1])
                if not (index_1 == m):
                    index_1 += 1
            #  elif (nums1[index_1] > nums2[index_2]):
                #  sorted_array.append(nums1[index_1])
                #  if not (index_1 == m):
                    #  index_1 += 1
            else:
                sorted_array.append(nums2[index_2])
                if not (index_2 == n):
                    index_2 += 1
            print(index_1, index_2, sorted_array)
            #  if len(sorted_array) >= 10:
                #  break
        for i in range(len(sorted_array)):
            nums1[i] = sorted_array[i]

if __name__ == "__main__":
    sol = Solution()
    #  base
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    #  wrong
    #  nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
    #  m = 5
    #  nums2 = [-1,-1,0,0,1,2]
    #  n = 6

    sol.merge(nums1, m, nums2, n)
    print(nums1)
