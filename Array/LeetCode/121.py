from typing import List


# 브루트 포스 -> 타임 아웃
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            profit = max(profit, (max(prices[i + 1:]) - prices[i]))

        return profit
'''

# 저점 vs 현재값 -> 저점 갱신
# 이득 vs 현재값-저점 -> 이득 갱신

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPri = 10 ** 4
        profit = 0

        for price in prices:
            minPri = min(minPri, price)
            profit = max(profit, price - minPri)

        return profit
