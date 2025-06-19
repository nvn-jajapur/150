from typing import List
class Solution:
    def findCeleb(self,matrix: List[List[int]]):
        for i in range(len(matrix[0])):
            sum =0
            for row in matrix:
                sum+=row[i]
                if sum == len(matrix[0])-1:
                    return i
        return -1



if __name__ =="__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = [[0,1,1,0],[0,0,0,0],[0,1,0,0],[1,1,0,0]]
    sol = Solution()
    print(sol.findCeleb(matrix))
        