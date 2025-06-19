def merge_sort(arr:[],low:int, high:int):
    mid = (low +high) //2
    if low >=high:
        return
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low, mid, high)

def merge(arr:[], low:int, mid:int, high:int):
    left = low
    right = mid+1
    count=0
    temp = []
    while ( left <=mid and right <= high):
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            count += (mid-left)+1
            right+=1
    while (left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
    arr[low:high+1]=temp
    print(count)
    


if __name__=='__main__':
    lst = [3,7,4,1,2]
    merge_sort(lst,0,len(lst)-1)
    print(lst)   