from typing import List
'''
start with the element at 0 index as minimum
now swap the values which are lesser than the value at min and 
by the end first lowest will be at the correct pos and rest will continue
'''
def selection(arr : List[int]):
        for i in range(len(arr)):
                min =i
                for j in range(i,len(arr)):
                        if arr[j]<arr[min]:
                               min = j
                arr[min],arr[i]=arr[i],arr[min]
        return arr
brr = [4,7,3,0,1,9]
print(selection(brr))
'''
Time complexity is : O(N^2)
Space Complexity : O(1)
'''