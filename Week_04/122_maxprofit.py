from typing import List


# 自己第一遍做，使用的是比较直观的方法，找买点和卖点，然后加差值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        money, buy = 0, 0
        # 0 应该买，1应该要卖
        flag = 0
        n = len(prices)
        for i in range(n):
            if i < n-1:
                # 该买了
                if flag == 0 and prices[i+1] > prices[i]:
                    buy = prices[i]
                    flag = 1
                    continue
                if flag == 1 and prices[i+1] < prices[i]:
                    money += (prices[i] - buy)
                    flag = 0
            if flag == 1 and i == n-1:
                if flag == 1 and prices[i-1] <= prices[i]:
                    print(prices[i], buy)
                    money += prices[i] - buy
        return money