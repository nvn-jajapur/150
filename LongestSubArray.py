def longest_sub_arry_better(arr:[],k)->int:
   sum,maxLen=0,0
   sumMap={}
   for i,v in enumerate(arr):
      sum+=v
      if sum ==k:
         maxLen=max(sum,i+1)
      rem = sum-k # if sum is 9 then we are looking for the remainder key 6 in the map which would be the answer
      if sumMap.get(rem):
         length = i-sumMap[rem]
         maxLen = max(maxLen,length)
      if sum not in sumMap: 
         # here checking the map if the key is already present, if yes, we should not update the value because if it contains
         # 0's then it would update the value which is incorrect
         # check for arr=[2,0,0,3] and k =3 without checking the key
         sumMap[sum]=i
   return maxLen
'''
Here Timne complexity is O(N*logN) : N for the for loop and LogN for searching the keys in Hash Map
'''
def longest_sub_array_optimal(arr:[],k:int)->int:
   leftP,rightP=0,0
   sum=arr[0]
   n=len(arr)
   maxLen=0
   while rightP<n: #RightP goes along the array to check the value where previous sum exceeds k
      while(leftP<=rightP and sum>k): # the leftP would decrement from the left if the sum > k and it should be less than rightP
         sum-=arr[leftP]
         leftP+=1
      if sum ==k:
         maxLen=max(maxLen,(rightP-leftP)+1)
      rightP+=1
      if rightP<n:# check rightP bcoz it may exceed the N
         sum+=arr[rightP]
   return maxLen
'''
Here Time Complexity is O(2*N)
First N - for the rightP loop 
Second N does not run for N times as it is sub array of rightP Loop so at max itt runs for N
'''

if __name__ == "__main__":
    arr=[1,2,3,1,1,1,9,8,0,0,1,1,1,1]
    print(longest_sub_array_optimal(arr,4))
   #  print(longest_sub_arry_better(arr,4))
