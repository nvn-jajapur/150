import math
def smallest_divisor(arr:[], k :int)->int:
    low =1
    high = max(arr)
    divi = 0
    while(low <=high):
        mid = (low +high)//2
        for i in arr:
            divi += math.ceil(i/mid)
        if (divi<=k):
            high = mid-1
            divi =0
        else:
            low = mid+1
            divi=0
    return low

def sumByD(arr, div):
    n = len(arr)  # size of array
    # Find the summation of division values
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def smallestDivisor(arr, limit):
    n = len(arr)
    if n > limit:
        return -1
    low = 1
    high = max(arr)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__ == '__main__':
    arr = [44,22,33,11,1]
    print(smallest_divisor(arr,5))
    # print(smallestDivisor(arr,5))