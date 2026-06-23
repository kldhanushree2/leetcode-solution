"""You are given two strings word1 and word2.
 Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string."""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        l=len(word1) if len(word1)<len(word2) else len(word2)
        for i in range(l):
            res+=word1[i]
            res+=word2[i]
            i+=1
        if(l==len(word1)):
            for i in range(l,len(word2)):
                res+=word2[i]
        else:
            for i in range(l,len(word1)):
                res+=word1[i]
        return res