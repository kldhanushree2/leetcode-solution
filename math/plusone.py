"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's."""

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
        