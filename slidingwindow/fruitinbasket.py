"""Given an integer array fruits where fruits[i] is the type of fruit the i-th tree produces, you want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        left = 0
        ans = 0

        for right in range(len(fruits)):
            d[fruits[right]] = d.get(fruits[right], 0) + 1

            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans