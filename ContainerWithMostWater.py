from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low =0
        high = len(heights)-1
        ans =0
        while(low <high):
            minimium = min(heights[low],heights[high])
            x =  (high-low) * minimium
            ans = max(ans,x)
            if (heights[low] <=heights[high]):
                low +=1
            else: high-=1
        return ans
if __name__ =='__main__':
    arr = [1,7,2,5,4,7,3,6]
    sol = Solution()
    print(sol.maxArea(arr))