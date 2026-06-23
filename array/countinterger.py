"""given an integer array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers."""
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        m=0
        n=0
        for i in nums:
            if i>0:
                m+=1
            elif i<0:
                n+=1
        s= m if m>=n else n
        return s