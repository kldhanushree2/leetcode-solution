"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise."""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        for i in range(len(t)):
            if j < len(s) and t[i]==s[j]:
                    j+=1       
        return j==len(s)