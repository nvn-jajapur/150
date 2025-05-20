def bubblesort(arr):
    '''
    Here the i loop would be starting from the last and 
    j loop ill be from 0 to i and compare the adjacent elements and swap if arr[j] > arr[j+1]
    by the end of first iteration max will be at the last
    '''
    for i in range(len(arr)-1, 0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
x = [5,7,3,1,2]
print(bubblesort(x))
'''
Time complexity : O(N^2)
Space complexity : O(1)
'''