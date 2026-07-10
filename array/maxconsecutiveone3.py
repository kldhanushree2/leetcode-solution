"""given a binary array nums and an integer k, you can flip at most k 0's to 1's. Return the length of the longest (contiguous) subarray that contains only 1's."""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        z=0
        m=0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            while(z>k):
                if nums[l]==0:
                    z-=1
                l+=1
            if(z<=k):
                m=max(m,r-l+1)
                r+=1
        return m