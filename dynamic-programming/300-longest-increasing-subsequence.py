class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        length_sub = []
        for i in range(len(nums)):
            length_sub.append(1)
        #  print(length_sub)
        for i in range(len(nums)):
            if i != 0:
                max_len = 1
                for j in range(i):
                    #  print(j, length_sub[j], length_sub[i])
                    if nums[j] < nums[i]:
                        cur_len = length_sub[j] + 1
                        #  print(cur_len)
                        if cur_len > max_len:
                            max_len = cur_len
                length_sub[i] = max_len
                #  print(length_sub)
        return max(length_sub)

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
