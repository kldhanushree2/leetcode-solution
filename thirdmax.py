"""Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number."""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums)
        l=list(s)
        l.sort()
        if(len(l)>=3):
            return l[-3]
        return l[-1]