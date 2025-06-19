def lower_bound(arr,k)->int:
    n =len(arr)
    ans = n
    low = 0
    high = n-1
    while(low <= high):
        mid = (low + high)//2
        if (arr[mid] >= k):
            ans = mid
            high = mid -1
        else:
            low = mid + 1
    return ans

def upper_bound(arr,k)->int:
    n =len(arr)
    ans = n
    low = 0
    high = n-1
    while(low <= high):
        mid = (low + high)//2
        if (arr[mid] > k):
            ans = mid
            high = mid -1
        else:
            low = mid + 1
    return ans

if __name__ == "__main__":
    arr = [1,2,4,6,7,8,8,8,10]
    print(lower_bound(arr,8))
    print(upper_bound(arr,8))