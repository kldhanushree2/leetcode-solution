"""Given the customers array and the grumpy array, return the maximum number of customers that can be satisfied after using the technique for minutes minutes."""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s=0
        su=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                s+=customers[i]
        for i in range(minutes):
            if grumpy[i]==1:
                su+=customers[i]
        m=su
        for i in range(minutes,len(grumpy)):
            if grumpy[i-minutes]==1:
                su-=customers[i-minutes]
            if grumpy [i]==1:
                su+=customers[i]
            if m<su:
                m=su
        return s+m