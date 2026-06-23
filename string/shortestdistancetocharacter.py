class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l=[]
        ans=[]
        for i in range(len(s)):
            if(s[i]==c):
                l.append(i)
        for j in range(len(s)):
            li=[]
            for t in l:
                dis=abs(t-j)
                li.append(dis)
            t=min(li)
            ans.append(t)
            li.clear()
        return ans