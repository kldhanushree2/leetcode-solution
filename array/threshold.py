"""given an integer array arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold."""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c=0
        s=0
        for i in range(k):
            s+=arr[i]
        av=s//k
        if av>=threshold:
            c+=1
        for i in range(k,len(arr)):
            s-=arr[i-k]
            s+=arr[i]
            av=s//k
            if av>=threshold:
                c+=1
        return c