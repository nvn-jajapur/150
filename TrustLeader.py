from collections import defaultdict
import collections
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        self.count =0
        dq = collections.deque()
        n = len(grid)
        m= len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.append((i,j,0))
                    visited.add((i,j))
        while dq:
            row, col, index = dq.popleft()
            self.count = max(self.count, index)
            rows = [-1,0,1,0]
            cols = [0,1,0,-1]
            for i in range(4):
                nrow = row + rows[i]
                ncol = col + cols[i]
                if  nrow<len(grid) and nrow >=0 and ncol >=0 and ncol < len(grid[0]) and (nrow, ncol) not in visited and grid[nrow][ncol] ==1:
                    dq.append((nrow,ncol, index + 1))
                    visited.add((nrow, ncol))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] !=2 and (i,j) not in visited and grid[i][j] !=0:
                    return -1
        return self.count
if __name__ == "__main__":
    n=4
    trust=[[1,2]]
    sol= Solution()
    print(sol.orangesRotting(trust))