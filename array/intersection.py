"""Given two integer arrays nums1 and nums2, return an array of their intersection.
 Each element in the result must be unique and you may return the result in any order."""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            for j in nums2:
                if(i==j):
                    l.append(i)
        li=set(l)
        lis=list(li)
        return lis