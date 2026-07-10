"""given a circular array code of length n, where code[i] represents the ith code, and an integer k, you need to replace every code[i] with the sum of the next k codes if k > 0, or the sum of the previous k codes if k < 0. 
If k == 0, replace code[i] with 0."""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        for i in range(n):
            s = 0

            if k > 0:
                for j in range(1, k + 1):
                    s += code[(i + j) % n]
            else:
                for j in range(1, abs(k) + 1):
                    s += code[(i - j) % n]

            ans[i] = s

        return ans