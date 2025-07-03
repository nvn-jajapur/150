from typing import List
def secondLargest(arr:[])->int:
    l=arr[0]
    sl=-1
    for i,v in enumerate(arr):
        if l<v:
            sl=l
            l=v
        if sl<v and l!=v:
            sl=v
    return sl
def checkSorted(arr:[])->bool:
    for i,v in enumerate(arr[0:len(arr)-1]): # arr[:-1] will give us all the elements expect the last element
        if v<= arr[i+1]:
            continue
        else:
            return False 
    return True  
def remove_duplicates_from_the_sorted_array(arr:[])->[]:
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
    return arr
def left_rotate(arr:[],k:int)->[]:
    while k>0:
        temp=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[len(arr)-1]=temp
        k-=1
    return arr
def right_rotate(arr:[],k:int)->[]:
    k=k%len(arr)
    while k>0:
        temp =arr[len(arr)-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
        k-=1
    return arr

def move_zeros(arr:[])->[]:
    j=-1
    for i in range(len(arr)-1):
        if arr[i]==0:
            j=i
            break
    for x in range(j+1,len(arr)-1):
        if arr[x]!=0:
            arr[j],arr[x]=arr[x],arr[j]
            j+=1
    return arr
    

def linear_search(arr:[],k:int)->int:
    for i in range(len(arr)-1):
        if arr[i]==k:
            return i
    return -1
def union_array(arr1:[],arr2:[])->[]:
    n1,n2 = len(arr1),len(arr2)
    i,j=0,0
    union =[]
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            if i not in union or union[-1]!=arr1[i]:
                union.append(arr1[i])
            i+=1
        else:
            if j not in union or union[-1]!=arr2[j]:
                union.append(arr2[j])
            j+=1
    while i<n1:
        if i not in union or union[-1]!=arr1[i]:
            union.append(arr1[i])
        i+=1
    while j<n2:
        if j not in union or union[-1]!=arr2[j]:
            union.append(arr2[j])
        j+=1
    return union

def intersection(arr1:[], arr2:[])->[]:
    n1,n2 = len(arr1),len(arr2)
    i,j=0,0
    intersect=[]
    while i<n1 and j<n2:
        if arr1[i] == arr2[j]:
            intersect.append(arr1[i])
            i+=1
            j+=1
        elif arr2[j]>arr1[i]:
            i+=1
        else:
            j+=1
    return intersect
            

def checkMissingNumber(arr:[])->int:
    # hash=[0]*(len(arr)+1)
    # for i in range(0,len(arr)-1):
    #     hash[arr[i]]=1
    # for i in range(1,len(hash)-1):
    #     if hash[i]==0:
    #         return i
    """
    Here sum would take high memeory if N is very very lareg
    sum = (len(arr)*(len(arr)+1))//2
    temp=0
    for i in range(len(arr)-1):
        temp+=arr[i]
    return sum-temp
    """
    xor1,xor2=0,0
    for i in range(0,len(arr)-1):
        xor1^=arr[i]
        xor2^=(i+1)
    xor2=xor2^len(arr)
    return xor2^xor1
def count1s(arr:[])->int:
    maximum,count=0,0
    for i,v in enumerate(arr):
        if v==1:
            count+=1
        else:
            if count > maximum:
                maximum=count
            count=0
    return maximum
def findone(arr:[])->int:
    xor =0
    for i,v in enumerate(arr):
        xor^=v
    return xor

def removeDuplicates( nums: List[int]) -> int:
        mySet = set(nums)
        nums = tuple(mySet)
        print(nums)
        return len(mySet)
        

            

if __name__ == "__main__":
    arr=[1,1,2,3,5,3,2]
    brr = [0,1,2,3,4]
    # print(secondLargest(arr))
    # print(checkSorted(arr))
    # print(remove_duplicates_from_the_sorted_array(arr))
    #print(left_rotate(arr,2))
    # print(right_rotate(arr,5))
    # print(move_zeros(arr))
    #print(linear_search(arr,0))
    # print(union_array(arr,brr))
    # print(intersection(arr,brr))
    # print(checkMissingNumber(arr))
    # print(count1s(arr))
    # print(findone(arr))
    print(removeDuplicates(arr))