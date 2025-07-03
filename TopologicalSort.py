# FInding the shortest path in a Directed Acyclic Graph


# Using BFS Topological Sort

from typing import List
import collections

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(V)]
        indegree =[0]*V
        for src, dest, wt in edges:
            adj[src].append((dest,wt))
            indegree[dest]+=1
        visited = [0]*V
        dq = collections.deque()
        for i in range(V):
            if indegree[i] ==0:
                dq.append(i)
        res =[]
        dist = [1e9]*V
        dist[0]=0
        while dq:
            node = dq.popleft()
            res.append(node)
            for i,j in adj[node]:
                indegree[i] -=1
                if indegree[i]==0:
                    dq.append(i)
        for u in res:                    # u is each node in topo order
            for dest, wt in adj[u]:      # now dest,wt is one edge
                if dist[u] + wt < dist[dest]:
                    dist[dest] = dist[u] + wt
        for i in range(len(dist)):
            if dist[i]== 1e9:
                dist[i] =-1
        return dist


# Using DFS Topological Sort

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(V)]
        for src, dest, wt in edges:
            adj[src].append((dest,wt))
        visited = [0]*V
        st=[]
        def dfs(node):
            visited[node]=1
            for i,j in adj[node]:
                if not visited[i]:
                    dfs(i)
            st.append(node)
        for i in range(V):
            if not visited[i]:
                dfs(i)
        dist = [1e9] * V
        dist[0]=0
        while st:
            node=st.pop()
            for i,j in adj[node]:
                if dist[node] + j < dist[i]:
                    dist[i] = dist[node] + j
        for i in range(len(dist)):
            if dist[i]== 1e9:
                dist[i] =-1
        return dist
