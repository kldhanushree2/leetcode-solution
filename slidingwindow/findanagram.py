"""given a string s and a non-empty string p, find all the start indices of p's anagrams in s."""

class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []
        d1 = {}
        d2 = {}
        for ch in p:
            d1[ch] = d1.get(ch, 0) + 1
        k = len(p)
        for ch in s[:k]:
            d2[ch] = d2.get(ch, 0) + 1
        ans = []
        if d1 == d2:
            ans.append(0)
        for i in range(k, len(s)):
            add_char = s[i]
            remove_char = s[i - k]
            d2[add_char] = d2.get(add_char, 0) + 1
            d2[remove_char] -= 1
            if d2[remove_char] == 0:
                del d2[remove_char]
            if d1 == d2:
                ans.append(i - k + 1)
        return ans