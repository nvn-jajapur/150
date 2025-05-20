def merge_sort(arr:[],low:int,high:int)->None:
    mid =(low+high)//2
    if low>=high:
        return
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
def merge(arr:[],low:int,mid:int,high:int)->None:
    leftP,rightP=low,mid+1
    temp=[]
    while (leftP<=mid and rightP<=high): # the loop should not exceed the lmit
        if arr[leftP]<=arr[rightP]:
            temp.append(arr[leftP])
            leftP+=1
        else:
            temp.append(arr[rightP])
            rightP+=1
    # while leftP<=mid:
    #     temp.append(arr[leftP])
    #     leftP+=1
    # while rightP<=high:
    #     temp.append(arr[rightP])
    #     rightP+=1
    temp.extend(arr[leftP:mid+1])
    temp.extend(arr[rightP:high+1])

    arr[low:high+1] = temp # we need to assign back to original array as recursive and we are not return the main arr

    
if __name__ == "__main__":
    lst =[1,2,3,4]
    merge_sort(lst,0,len(lst)-1)
    print(lst)
'''
Time complexity : O(N*logN)
Space complexity : O(N)
'''
