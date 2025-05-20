def insertion(arr):
    '''
    Here the i loop starts from o to n
    and in j would take the i position at first at checks the elements backwards ad=nd swaps it if it is higher 
    i.e. arr[j-1]>arr[j]
    '''
    for i in range(len(arr)):
        j=i
        while(j>0) and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1

    return arr
x = [5,7,3,1,2]
print(insertion(x))
'''
Time complexity : O(N^2)
Space complexity : O(1)
'''

