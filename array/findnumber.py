"""Given an array nums of integers, return how many of them contain an even number of digits."""
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        m=0
        for i in nums:
            s=len(str(i))
            if(s%2==0):
                m+=1
        return m