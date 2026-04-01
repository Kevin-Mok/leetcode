class Solution:
    def minPartitions(self, n: str) -> int:
        num = int(n)
        nums_needed = 0
        while num > 0:
            num_str = str(num)
            num_subtract = "1" * len(num_str)
            num_subtract_list = list(num_subtract)
            for i in range(len(num_str)):
                if num_str[i] == "0":
                    num_subtract_list[i] = "0"
                    print(num, num_subtract_list)
            num_subtract = ''.join(num_subtract_list)
            num = num - int(num_subtract)
            print(num, num_subtract)
            nums_needed += 1
        return nums_needed
        #  return max(list(n))
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.minPartitions("32"))
    print(sol.minPartitions("82734"))
    print(sol.minPartitions("27346209830709182346"))
