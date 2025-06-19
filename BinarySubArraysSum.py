from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.sumofArrays(nums,goal) - self.sumofArrays(nums,goal-1)
    def sumofArrays(self, arr:[], k :int)->int:
        if(k<0): return 0
        l=r=count=sum=0
        while(r<len(arr)):
            sum+=arr[r]
            while(sum > k):
                sum-=arr[l]
                l+=1
            count+=(r-l+1)
            r+=1
        return count


if __name__ =='__main__':
    sol = Solution()
    arr = [0,0,0,0,0]
    print(sol.numSubarraysWithSum(arr,0))