def fourSum(arr:[],target:int)->[]:
    ansSet=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            set1=set()
            for k in range(j+1,len(arr)):
                sum = target -(arr[i] + arr[j] +arr[k])
                if sum in set1:
                    temp = [arr[i], arr[j], arr[k], sum]
                    temp.sort()
                    ansSet.add(tuple(temp))
                set1.add(arr[k])
    return list(ansSet)

''''
Time Complexity : O(N3) * O(NlogN)
Space Complexity : O(N)
'''

'''
In the Optimal approach, We are sorting the array firstand using the two pointer technique
i,j are fixed and k,l are moving pointers
'''
def fourSumOptimal(arr:[], target :int)->[]:
    ans=[]
    arr.sort()
    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr)):
            if j>i+1 and arr[j] == arr[j-1]:
                continue
            k =j+1
            l=len(arr)-1
            while(k<l):
                sum = arr[i]+arr[j]+arr[k]+arr[l]
                if (sum == target):
                    temp = [arr[i],arr[j],arr[k],arr[l]]
                    ans.append(temp)
                    k+=1
                    l-=1
                    while(k<l and arr[k] == arr[k-1]):
                        k+=1
                    while ( k<l and arr[l]== arr[l+1]):
                        l-=1
                elif (sum>0):
                    l-=1
                else:
                    k+=1

    return ans
''''
Time Complexity : O(N3)
Space Complexity : O(Temp)
'''
if __name__ =="__main__":
    arr =[1,-1,0,2,3,0,1]
    # print(fourSum(arr,1))
    print(fourSumOptimal(arr,1))