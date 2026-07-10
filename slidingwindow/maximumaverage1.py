"""Given an integer array nums consisting of n elements, find the contiguous subarray of given length k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted."""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        for i in range (k):
            s+=nums[i]
        av=float(s/k)
        m=av
        for i in range(k,len(nums)):
            s-=nums[i-k]
            s+=nums[i]
            av=float(s/k)
            if m<av:
                m=av
            
        return m