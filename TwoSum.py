'''
It is a better approach as it using extra space of map
'''
def two_sum_better (arr:[],k:int)->bool:
    hmap = {}
    for i,v in enumerate(arr):
        target = k-v
        if target in hmap:
            return True
        hmap[v]=i
    return False
'''
Time complexity : O(N*logN)
Space Complexity : O(N)
'''
''' Th below is optimal approach as we are not suing extra space'''
def two_sum_optimal(arr:[],k:int)->bool:
    arr.sort()
    i,j=0,len(arr)-1
    while(i<j):
        sum = arr[i]+arr[j]
        if sum == k:
            return True
        elif (sum > k):
            j-=1
        
        else:
            i+=1
    return False

if __name__ == "__main__":
    lst = [2,6,8,0,1]
    # print(two_sum_optimal(lst,11))
    print(two_sum_better(lst,0))
'''
Time Complexity : O(N) + O(NlogN) as we are sorting the array
Space Complexity : O(1)
'''