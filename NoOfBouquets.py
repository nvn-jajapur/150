
def possible_bouquets(arr:[],limit:int,m:int,k:int)->bool:
    count =0
    noOfB=0
    for i in range(len(arr)):
        if(arr[i]<=limit):
            count+=1
        else:
            noOfB += (count)/k
            count=0
    noOfB += (count / k)
    return noOfB >=m


def find_no_of_bouquets(arr:int,m:int,k:int):
    low = min(arr)
    high = max(arr)
    while (low <=high):
        mid = (low + high)//2
        if(possible_bouquets(arr,mid,m,k)):
            high = mid-1
        else: low = mid+1
    return low
if __name__ == '__main__':
    arr = [7,7,7,7,13,11,12,7]
    print(find_no_of_bouquets(arr,2,3))