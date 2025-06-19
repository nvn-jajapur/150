from typing import List
class MergeOverLappingIntervals:
    def merge_overlapping_intervals(self,arr:List[List[int]])->List[List[int]]:
        ans =[]
        for i in range(len(arr)):
            if not ans or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            else:
                ans[-1][1] = max (ans[-1][1], arr[i][1])
        return ans

if __name__ =="__main__":
    arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
    sol = MergeOverLappingIntervals()
    print(sol.merge_overlapping_intervals(arr))


