"""You are given an array prices where prices[i] is the price of a given stock on the ith day."""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       mi=prices[0]
       ma=0
       for i in prices:
          mi=min(mi,i)
          ma=max(ma,i-mi)
       return ma