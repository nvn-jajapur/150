def arry_rotated(arr:[])->int:
    low = 0
    high = len(arr)-1
    val =10000
    while(low<=high):
        mid = (low + high)//2
        if (arr[low] <= arr[mid]):
            val = min(arr[low], val)
            low = mid+1
        else:
            high = mid-1
            val = min(val, arr[mid])
    return val

def arry_rotated_index(arr:[])->int:
    low = 0
    high = len(arr)-1
    val =10000
    index = -1
    while(low<=high):
        mid = (low + high)//2
        if (arr[low] <= arr[mid]):
            if (val > arr[low]):
                val = arr[low]
                index = low
            low = mid+1
        else:
            high = mid-1
            if (val > arr[mid]):
                val = arr[mid]
                index = mid

    return index

if __name__ =="__main__":
    arr = [3,5,6,0,1,2]
    print(arry_rotated(arr))
    print(arry_rotated_index(arr))