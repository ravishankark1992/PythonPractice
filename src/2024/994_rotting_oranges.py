from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        direction = [(1,0), (-1, 0), (0, 1), (0,-1)]
        all_rotten = deque()
        fresh_count = 0
        visited=[]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==ROTTEN:
                    all_rotten.append((i,j))
                elif grid[i][j] == FRESH:
                    fresh_count+=1
        if fresh_count==0:
            return 0
        minutes = 0
        new_rotten=deque()
        while len(all_rotten)>0:
            curr_node = all_rotten.popleft()
            if curr_node not in visited:
                visited.append(curr_node)
            for action in direction:
                new_node = (curr_node[0]+action[0], curr_node[1]+action[1])
                x,y = new_node
                if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]):
                    if new_node not in visited:
                        visited.append(new_node)
                        if grid[x][y]==FRESH:
                            fresh_count-=1
                            new_rotten.append(new_node)
            
            if len(all_rotten)==0:
                minutes+=1
                all_rotten=new_rotten
                new_rotten=deque()
                    
        if fresh_count>0:
            return -1
        else:
            return minutes-1
        
o=Solution()
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid=[[0,2]]
print(o.orangesRotting(grid))