def quick_sort(arr:[],low:int,high:int):
    '''
    Here we take a pivot element and find the correct position of it.
    Once we find this index, the elements on left of it will be lower than pivot and 
    the elements on the right would be greater than the pivot.

    We continue the same for left sub array and right sub array using recursion
    '''
    if low<high:
        index = partition(arr,low,high)
        quick_sort(arr,low,index-1)
        quick_sort(arr,index+1,high)
def partition(arr:[],low:int,high:int)->int:
    pivot = arr[low]
    i,j=low,high
    while i<j:
        while arr[i]<=pivot and i<=high-1: # here the loop runs i gets incremented until u find the first value which is GREATER than pivot
            # and here i<=high-1 because if we we put i<=high we would be checking i==4 and then we would be incrementing i to length + 1 and it would be out of bounds
            i+=1
        while arr[j]>=pivot and j>=low+1: # here the loop runs j gets decremented until u find the first value which is SMALLER than pivot
            j-=1 # here j>=low+1 because if we put j>=low then j would be going to j=0 and then decrement j by -1 which is out of bound
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[low]=arr[low],arr[j]
    return j
if __name__ == "__main__":
    lst =[4,3,2,1,5,5]
    quick_sort(lst,0,len(lst)-1)
    print(lst)
