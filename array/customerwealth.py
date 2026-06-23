"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has."""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for row in accounts:
            l.append(sum(row))
        return max(l)

