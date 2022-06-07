class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins_sub = []
        for i in range(amount + 1):
            coins_sub.append([])
            for j in range(len(coins)):
                if i == 0:
                    coins_sub[i].append(0)
                else:
                    coins_sub[i].append(amount + 1)
        #  print(coins, amount)
        #  print(coins_sub)

        for i in range(amount + 1):
            for j in range(len(coins)):
                #  uses_coin_num = 99999
                #  print(i, j)
                if (i - coins[j] >= 0):
                    #  uses_coin_num = i - j
                    #  print("insert")
                    use_coin = 1 + coins_sub[i - coins[j]][j]
                    not_use_coin = coins_sub[i][j - 1]
                    #  print(use_coin, not_use_coin)
                    coins_sub[i][j] = min(use_coin,
                            not_use_coin)
                else:
                    coins_sub[i][j] = coins_sub[i][j - 1]
                #  print(coins_sub)
        return (coins_sub[i][j] 
                if coins_sub[i][j] < amount + 1
                else -1)
