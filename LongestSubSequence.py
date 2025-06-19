def longest_sub_sequence(arr:[])->int:
    count=0
    retCount=0
    for i,v in enumerate(arr):
        f=v
        count=1
        while(linear_search(arr,f+1)):
            count+=1
            retCount=max(retCount,count)
            f+=1
        
    return retCount
def linear_search(arr:[],find:int)->bool:
    for i,v in enumerate(arr):
        if v==find:
            return True
    return False

def longest_sub_sequence_better(arr:[])->int:
    arr.sort()
    retCount=0
    lastSmall,count=arr[0],1
    for i,v in enumerate(arr):
        if (v==lastSmall+1):
            count+=1
            lastSmall=v
        else:
            count=1
            lastSmall=v
        retCount=max(count,retCount)
    return retCount

def longest_sub_sequence_optimal(arr:[])->int:
    arrSet = set(arr)
    count,retCount=0,0
    for i,v in enumerate(arrSet):
        if v+1 in arrSet:
            count=1
            nextEle = v
            while nextEle+1 in arrSet:
                count+=1
                nextEle+=1
            retCount=max(count,retCount)
    return retCount

if __name__ == "__main__":
    arr = [0,-1]
    # print(longest_sub_sequence(arr))
    # print(longest_sub_sequence_better(arr))
    print(longest_sub_sequence_optimal(arr))