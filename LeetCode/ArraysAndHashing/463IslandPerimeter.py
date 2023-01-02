# https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def CountSurround(x,y,grid) -> int:
            xmax = len(grid)-1
            ymax = len(grid[0])-1
            count=0
            if 0<=x-1<=xmax and grid[x-1][y]==1:
                count+=1
            if 0<=x+1<=xmax and grid[x+1][y] ==1:
                count+=1
            if 0<=y-1<=ymax and grid[x][y-1] ==1:
                count+=1
            if 0<=y+1<=ymax and grid[x][y+1] ==1:
                count+=1
            return count

        ans=0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    print(x,y,CountSurround(x,y,grid))
                    ans += 4-CountSurround(x,y,grid)
        return ans
            