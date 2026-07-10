"""Given an integer array nums and an integer k, return the maximum sum of a subarray of size k with all distinct elements. If there is no such subarray, return 0."""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s=0
        d={}
        m=0
        for i in range(k):
            if nums[i] in d:
                d[nums[i]]=d.get(nums[i],0)+1
            else:
                d[nums[i]]=1
            s+=nums[i]
        if m<s and (len(d)==k):
            m=s
        for i in range(k,len(nums)):
            if d[nums[i-k]]==1:
                s-=nums[i-k]
                del d[nums[i-k]]
            else:
                s-=nums[i-k]
                d[nums[i-k]]-=1

            if nums[i] in d:
                d[nums[i]]=d.get(nums[i],0)+1
            else:
                d[nums[i]]=1
            s+=nums[i]
            if m<s and (len(d)==k):
                 m=s  
           
        return m