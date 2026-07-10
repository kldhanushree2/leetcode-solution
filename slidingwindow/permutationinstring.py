"""Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
 In other words, one of the first string's permutations is the substring of the second string."""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d1 = {}
        d2 = {}
        for ch in s1:
            d1[ch] = d1.get(ch, 0) + 1
        k = len(s1)
        for ch in s2[:k]:
            d2[ch] = d2.get(ch, 0) + 1
        if d1 == d2:
            return True
        for i in range(k, len(s2)):
            add_char = s2[i]
            remove_char = s2[i - k]

            d2[add_char] = d2.get(add_char, 0) + 1

            d2[remove_char] -= 1
            if d2[remove_char] == 0:
                del d2[remove_char]

            if d1 == d2:
                return True

        return False