"""Given a m x n integer array grid where grid[i][j] could be:"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        count=0
        def findpath (i,j,sol,step):
            nonlocal count
            if i<0 or i>=n or j<0 or j>=m or sol[i][j]==1 or grid[i][j]==-1:
                return False
            if grid[i][j]==2 and sol[i][j]==0:
                if c==step:
                    count=count + 1
                return False

            sol[i][j]=1

            if findpath(i+1,j,sol,step+1):
                return True
            if findpath(i,j+1,sol,step+1):
                return True
            if findpath(i-1,j,sol,step+1):
                return True
            if findpath(i,j-1,sol,step+1):
                return True

            sol[i][j]=0
            return False
        c=0
        a=[]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    a.append(i)
                    a.append(j)
                if grid[i][j]!=-1:
                    c+=1
        sol=[[0]*m for _ in range(n)]
        findpath(a[0],a[1],sol,1)
        print (c)
        return count
