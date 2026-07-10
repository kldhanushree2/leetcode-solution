"""Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k."""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        for i in range(k):
            if s[i] in "aeiou":
                c+=1
        m=c
        for i in range(k,len(s)):
            if s[i-k] in "aeiou":
                c-=1
            if s[i] in "aeiou":
                c+=1
            if c>m:
                m=c
        return m
        