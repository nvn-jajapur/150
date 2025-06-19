from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        maxArea=0
        for i,v in enumerate(heights):
            while stack and(i==len(heights) or heights[stack[-1]] >=v):
                index = stack.pop()
                nse = i
                pse = -1 if not stack else  stack[-1]
                maxArea = max ( maxArea, (nse - pse -1) * heights[index])
            stack.append(i)
        while stack:
            nse = len(heights)
            val = stack.pop()
            pse = -1 if not stack else  stack[-1]
            maxArea = max ( maxArea, (nse - pse -1) * heights[val])
        return maxArea


if __name__  == '__main__':
    arr = [7,1,7,2,2,4]
    sol = Solution()
    print(sol.largestRectangleArea(arr))