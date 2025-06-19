from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea=0
        n = len(matrix)
        m = len(matrix[0])
        pSum =[[0] * m for _ in range(n)]
        for j in range(m):
            sum=0
            for i in range(n):
                sum+=int(matrix[i][j])
                if int(matrix[i][j]) ==0: sum=0
                pSum[i][j] = sum
        for i in range(n):
            maxArea = max(maxArea, self.largestHist(pSum[i]))
        return maxArea
    def largestHist(self, arr:[])->int:
        maxArea=0
        n = len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and (i==n or arr[stack[-1]] >= arr[i]):
                val = stack.pop()
                nse = i
                pse = -1 if not stack else stack[-1]
                maxArea = max(maxArea, arr[val] * (nse - pse -1))
            stack.append(i)
        while stack:
            nse = n
            val = stack.pop()
            pse = -1 if not stack else stack[-1]
            maxArea = max(maxArea, arr[val] * (nse - pse -1))
        
        return maxArea

if __name__ =="__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    sol = Solution()
    print(sol.maximalRectangle(matrix))
        