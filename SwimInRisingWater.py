from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dist = [[1e5]*cols for _ in range(rows)]
        dist[0][0] =0
        minHeap =[]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        heapq.heappush(minHeap, (grid[0][0], 0, 0))
        while minHeap:
            src, r, c = heapq.heappop(minHeap)
            if r==rows-1 and c == cols-1:
                return src
            for i in range(4):
                nr = r + dr[i]
                nc = c+ dc[i]
                if nr>=0 and nc >=0 and nr<rows and nc <cols:
                    maxD = max(src, grid[nr][nc])
                    if maxD < dist[nr][nc]:
                        dist[nr][nc]= maxD
                        heapq.heappush(minHeap, (maxD,nr,nc))
        return -1
if __name__ == '__main__':
    edges = [[3,2],[0,1]]
    sol = Solution()
    print(sol.swimInWater(edges))