"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            l.append(i*i)
        l.sort()
        return l