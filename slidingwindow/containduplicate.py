"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k."""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
        s = set()
        l = 0

        for i in range(len(nums)):
            if nums[i] in s:
                return True

            s.add(nums[i])

            if len(s) > k:
                s.remove(nums[l])
                l += 1

        return False