"""Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
 The digits are stored such that the most significant digit is at the head of the list, and each element in the
 array contains a single digit. You may assume the integer does not contain any leading zero, except the number 0 itself."""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for i in digits:
            n=n*10+i
        n+=1
        l=[]
        while(n>0):
            d=n%10
            l.append(d)
            n//=10
        l.reverse()
        return l        
        