def find_element_in_rotated_sorted_array(arr : [], k)-> int:
    n = len(arr)
    low = 0
    high = n-1
    while ( low <= high):
        mid = (low + high) //2
        if ( arr[mid] == k): return mid
        ## find out which side of array is sorted
        if ( arr[low] <= arr[mid]):
            if (k >=arr[low] and k <= arr[mid]):
                high = mid -1
            else:
                low = mid + 1
        else:
            if (arr[mid] <= k and k<=arr[high]):
                    low = mid+1
            else:
                high = mid-1

    return -1

def find_element_in_rotated_sorted_array1(arr:[], k) ->int:
    n = len(arr)
    low,high = 0, n-1
    while(low <= high):
        mid = (low + high)//2
        if ( arr[mid] == k): return mid
        ## check which part of array is sorted
        if ( arr[low] <= arr[mid]):
            if(k >=arr[low] and k<=arr[mid]):
                high = mid-1
            else:
                low = mid+1
        else:
            if(k>=arr[mid] and k<=arr[high]):
                low = mid+1
            else:
                high = mid -1
    return -1


if __name__ == "__main__":
    arr = [7,8,9,1,2,3,4,5,6]
    print(find_element_in_rotated_sorted_array1(arr,1))