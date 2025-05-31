'''
This is optimal approach

Here we are calculating the prefix sum and applying the x-k logic.
if we find the x in our hmap then the addition of elements until this position is equal to K 
so we are incrementing the count
while adding in to the map, we are just getting the count of prefixSum from the map and increment by 1

'''
def count_sum_of_sub_array(arr:[],k:int):
    count = 0
    hmap={}
    hmap[0]=1 # initilise the first element prefix sum as 0 as we are starting from first index and need to save this index
    prefixSum =0
    for i,v in enumerate(arr):
        prefixSum += v
        x = prefixSum-k # x-k logic
        count = count + hmap.get(x,0) # count how many prefix sums are present in the hmap
        hmap[prefixSum]= hmap.get(prefixSum,0)+1 # if sum is already present then directly update the count and add it to main count to return
    return count
'''
Time Complexity : O(N)
Space Complexity : O(1)
'''
if __name__=="__main__":
    arr = [1,2,3,-3,1,1,1,4,2,-3]
    print(count_sum_of_sub_array(arr,3))