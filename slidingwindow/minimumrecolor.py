"""You are given a string blocks consisting of n characters, each either 'W' or 'B', representing the colors of the blocks. 
You are also given an integer k, which is the desired number of consecutive black blocks."""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c=0
        for i in range(k):
            if(blocks[i]=='W'):
                c+=1
        m=c
        for i in range(k,len(blocks)):
            if blocks[i-k]=='W':
                c-=1
            if blocks[i]=='W':
                c+=1
            if m>c:
                m=c
        return m
        