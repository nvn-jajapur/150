def majority_element_better(arr:[],limit:int)->int:
    hmap={}
    for i,v in enumerate(arr):
        hmap[v]=hmap.get(v,0)+1
    for i in hmap:
        if hmap[i]>=limit:
            return i
    return -1
'''
Time Complexity : O(NlogN) + O(N) 
Space Complexity : O(N)
'''

## Moore's Voting Algorithm
'''
In this algorithm, the main logic is you would select the fisrt element as your majority element and then increment the count if 
you find it or decrement the count if you encounter any other element.
now you would follow the same for this new element by considering this as majority element and then following the same until you 
find the majority
The main idea behind this algo is,
if there exists as majority element, then the count of it would not cancel out to any other elements.

To check if the element that we have found by the end of the code, we would check if it is true by iteratinv over the array and checking
the count
if it is as per condition >(N/2)
then we would return this element 
if it is not then there would be no majority element

'''
def majority_element_optimal(arr:[])->int:
   ele, count=0,0
   for i,v in enumerate(arr):
       if count==0:
           ele=v
           count+=1
       elif ele ==v:
           count+=1
       else:
           count-=1
   count1=0
   for i,v in enumerate(arr):
       if v==ele:
           count1+=1
   if count1>(len(arr))/2:
       return ele
   return -1

'''
Time Complexity : O(N) + O(N)
Space Complexity : O(1)
'''

       
if __name__ == "__main__":
    arr = [2,1,3,4,2,2,1,2,2]
    # print(majority_element_better(arr,len(arr)/2))
    print(majority_element_optimal(arr))