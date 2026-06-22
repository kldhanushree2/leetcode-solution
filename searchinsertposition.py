"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 """
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=0
        for index,i in enumerate(nums):
            if(i==target):
                return index
            elif(i<target):
                n=index+1
        return n

        