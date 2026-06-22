"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l=list(range(0,nums[-1]+1))
        for i in range(len(l)):
            if nums[i]!=l[i]:
                return l[i]
        return l[-1]+1
