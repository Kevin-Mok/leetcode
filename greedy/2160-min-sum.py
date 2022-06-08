class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = list(str(num))
        num_list.sort()
        num_1 = ""
        num_2 = ""
        for i in range(len(num_list)):
            if i % 2 == 0:
                num_1 += num_list[i]
            else:
                num_2 += num_list[i]
        #  print(num_list)
        #  print(num_1, num_2)
        return int(num_1) + int(num_2)

if __name__ == "__main__":
    sol = Solution()
    sol.minimumSum(2932)
