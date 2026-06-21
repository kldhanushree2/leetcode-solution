"""Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward."""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        s=""
        for i in words:
            if i[:]==i[::-1]:
                s+=i
                break
        return s