class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        start =1
        count =0
        while maxDoubles:
            start+=1
            start*=2
            count+=1
            maxDoubles-=1
        while not (start == target):
            start+=1
            count+=1
        return count
if __name__ =='__main__':
    target =5
    maxDoubles =0
    sol = Solution()
    print(sol.minMoves(target, maxDoubles))