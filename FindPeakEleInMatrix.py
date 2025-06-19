from typing import List

class Solution:
    def maxEle(self, matrix : List[List[int]],row:int, col:int, mid:int):
        max =-1
        index =-1
        for i in range(row):
            if ( matrix[i][mid] > max):
                max = matrix[i][mid] 
                index =i
        return index



    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m =len(mat)
        n = len(mat[0])
        low = 0
        high = n-1
        while(low <=high):
            mid = (low + high)//2
            maxRowEle = self.maxEle(mat,m,n,mid)
            left = mat[maxRowEle][mid - 1] if (mid -1) >=0 else -1
            right = mat[maxRowEle][mid+1] if (mid +1) < m else -1
            if ( mat[maxRowEle][mid] > left and mat[maxRowEle][mid]>right ):
                return [maxRowEle, mid]
            elif mat[maxRowEle][mid] < right:
                low = mid+1
            else:
                high = mid -1
        return [-1,-1]
    

if __name__ == '__main__':
    arr = [[25,37,23,37,19],[45,19,2,43,26],[18,1,37,44,50]]
    sol = Solution()
    print(sol.findPeakGrid(arr))