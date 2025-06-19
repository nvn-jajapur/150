
def aggressive_cows(arr:[], k :int)->int:
    low = 1
    high = max(arr) - min(arr)
    while ( low <=high):
        mid = (low + high)//2
        if (can_we_place(arr,mid,k)):
            low = mid+1
        else:
            high = mid -1
    return high

def can_we_place( arr:[], mid:int, limit:int)->bool:
    count =1
    last =arr[0]
    for i in range(1,len(arr)):
        if (arr[i] - last >= mid):
            count+=1
            last = arr[i]
        if ( count >= limit):
            return True
    
    return False

if __name__ == '__main__':
    arr = [0,3,4,7,9,10]
    print(aggressive_cows(arr,4))