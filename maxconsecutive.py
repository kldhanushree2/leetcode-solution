"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        c=0
        for i in range(len(nums)):
            if(nums[i]==1):
                c+=1
                if m<c:
                    m=c
            else:
                c=0
        return m