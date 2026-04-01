from heapq import *
from math import floor

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        piles_heap = [-pile for pile in piles]
        heapify(piles_heap)
        for i in range(k):
            # negative
            max_pile_stones = heappop(piles_heap)
            rm_max_pile_stones = floor(abs(max_pile_stones) / 2)
            new_pile_stones = (abs(max_pile_stones) -
                               rm_max_pile_stones)
            heappush(piles_heap, -new_pile_stones)
            print(piles_heap)
        return int(sum([abs(pile) for pile in piles_heap]))


if __name__ == "__main__":
    sol = Solution()

    # 1
    piles = [5,4,9]
    k = 2
    answer = sol.minStoneSum(piles, k)
    print(answer)
