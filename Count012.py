

'''
This is a better solution as we are not using any extra space but there are multiple loops which would be takinh O(N) time
'''

def count0_1_2(arr:[])->[]:
    count0,count1,count2=0,0,0
    for i,v in enumerate(arr):
        if v==0:
            count0+=1
        elif v==1:
            count1+=1
        else:
            count2+=1 
    for i in range(0,count0):
        arr[i]=0
    for i in range(count0,count0+count1):
        arr[i]=1
    for i in range(count0+count1,len(arr)-1):
        arr[i]=2

    return arr

'''
Time Complexity : O(N+N)
Space Complexity : O(1)
'''


## Dutch National Flag Algorithm
'''
In this algo, there are three pointers
low, mid, and high

according to this algo, we have three parts 

first part : all 0's followed by all 1's i.e 0....1.....
second part : random unsorted 0's,1's,2's
thrid part : all 1's i.e. 1.....
final array = 000001111 210201.. 2222222
the pointer position would 
first part for 0's = 0 -> low-1
second part for 1's  = low -> mid-1
third part for random unsorted array = mid -> high-1
final oart for 2's = high -> n-1

The logic would as left and right are sorted we need to swap with positions to make it sort with the array
'''

def count0_1_2_optimal(arr:[])->[]:
    low,mid = 0,0 # assuming both mid and low would at same position of random array at the beginning
    high = len(arr)-1 

    while (mid<=high):
        if (arr[mid]==0): # if mid ele is 0 swap with low element and increment both mid and low
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid]==1: # if mid ele is 1, then just increment 1 as it is in correct order 
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid] # if mid ele is 2, then swap it with right array as it is sorted
            high-=1
    return arr
        
 '''
Time Complexity : O(N)
Space Complexity : O(1)
'''

if __name__=="__main__":
    arr = [0,0,0,0,1,2,0,0,1,1,2,2]
    # print(count0_1_2(arr))
    print(count0_1_2_optimal(arr))
