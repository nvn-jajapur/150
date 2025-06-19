
#### Kadanes Algorithm ######
'''
Here in this algorithm, we take the sum variable and only check for the positive sum  
If we encounter -ves, then we start again the sum for 0
If we encounter +ves, then we add the sum and which would be resultant answer
'''
import sys
def maximum_sub_array_sum(arr:[])->[]:
    sum=0
    maxSum = -sys.maxsize-1
    ansStart,end=-1,-1
    start=0

    for i,v in enumerate((arr)):
        if (sum==0):
            start=i
        sum+=v
        if sum>maxSum:
            maxSum=sum
            ansStart=start
            end=i
        if sum<0:
            sum=0
    return [maxSum,ansStart,end]
'''
Time Complexity : O(N)
Space Complexity : O(1)
'''
# If only sum is asked without the positions
def maximum_sub_array_sum1(arr:[])->int:
    sum=0
    maxSum=-sys.maxsize-1
    for i,v in enumerate(arr):
        sum+=v
        if sum>=maxSum:
            maxSum =sum
        if(sum<0):
            sum=0
    return maxSum

if __name__=="__main__":
    arr = [2,-3,4,-2,2,1,-1,4]
    print(maximum_sub_array_sum(arr))
    print(maximum_sub_array_sum1(arr))
'''
Time Complexity : O(N)
Space Complexity : O(1)
'''