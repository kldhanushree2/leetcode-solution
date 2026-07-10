"""Given an integer x, return true if x is a palindrome, and false otherwise."""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=x
        rev=0
        while(m>0):
            d=m%10
            rev=rev*10+d
            m//=10
        if rev==x:
            return True
        else:
            return False