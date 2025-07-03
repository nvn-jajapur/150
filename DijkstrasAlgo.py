from typing import List
import heapq
import collections
class Solution:
    def find_min_path_dijkstra(self,V: int, edges:List[List[int]], src:int)->[]: # type: ignore
        
        dist = [1e5]*V
        dist[src] = 0
        minHeap = []
        res =[]
        res.append(src)
        adj = [[] for i in range(len(edges))]
        for u,v,w in edges:
            adj[u].append((v,w))
        heapq.heappush(minHeap, (0,src))
        while minHeap:
            dis, node = heapq.heappop(minHeap)
            if dis > dist[node]:
                continue
            for dest, wt in adj[node]:
                nd = dis + wt
                if nd < dist[dest]:
                    dist[dest] = nd
                    heapq.heappush(minHeap, (nd, dest))
                    res.append(dest)
        print(res)
        return dist

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        source = (0,0)
        dest = (rowLength-1,rowLength-1)
        dq = collections.deque()
        dq.append((0,0,0))
        dist = [[1e9]*colLength for i in range(rowLength)]
        dist[0][0]=0
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        while dq:
            d, r, c = dq.popleft()
            for i in range(4):
                newr = r + dr[i]
                newc = c + dc[i]
                if ( newr >=0 and newr < rowLength and newc >=0 and newc < colLength and grid[newr][newc] ==0 and d + 1 < dist[newr][newc]):
                    dist[newr][newc] = d + 1
                    if (newr,newc) == dest:
                        return d + 1
                    dq.append((d +1, newr, newc))

        return -1

        

if __name__ == "__main__":
    v=5
    edges = [[0,1],[1,0]]#[[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
    src = 0
    sol = Solution()
    # print(sol.find_min_path_dijkstra(v,edges,src))
    print(sol.shortestPathBinaryMatrix(edges))