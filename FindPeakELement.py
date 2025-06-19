def find_peak_element(arr:[])->int:
    if (len(arr) ==1): return arr[0]
    if(arr[0]>arr[1]): return arr[0]
    if ( arr[len(arr)-1] > arr[len(arr)-2]): return arr[len(arr)-1]
    high = len(arr)-2
    low =1
    while(low<=high):
        mid = (low + high)//2
        if(arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
            return arr[mid]
        if ( arr[mid] > arr[mid-1]):
            low = mid+1
        else:
            high = mid-1
    return -1

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,8,12,13]
    print(find_peak_element(arr))