"""Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length."""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        l=[]
        while(i<j):
            if(numbers[i]+numbers[j]==target):
                l.append(i+1)
                l.append(j+1)
                break
            elif (numbers[i]+numbers[j]<target):
                i+=1
            else:
                j-=1
        return l