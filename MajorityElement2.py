'''
Use a small hashmap and get the count of the values
'''
def majority_element_better( ar:[])->int:
    hmap={}
    count=0
    for i,v in enumerate(ar):
        hmap[v]=hmap.get(v,0)+1
        if v in hmap and hmap[v] > ((len(ar)/3)):
            count+=1
    return count
'''
Time Complexity : O(N) + O(N)
Space Complexity : O(N)
'''



## Moore's Voting Algorithm
'''
In this algorithm, the main logic is you would select the fisrt element as your majority element and then increment the count if 
you find it or decrement the count if you encounter any other element.
But here we need to use two counters
now you would follow the same for this new element by considering this as majority element and then following the same until you 
find the majority
The main idea behind this algo is,
if there exists as majority element, then the count of it would not cancel out to any other elements.

To check if the element that we have found by the end of the code, we would check if it is true by iteratinv over the array and checking
the count
if it is as per condition >(N/3)
then we would return this element 
if it is not then there would be no majority element
'''
def majority_element_optimal(arr:[])->[]:
    ele1 = None
    ele2 = None
    cnt1,cnt2=0,0
    check_count1, check_count2=0,0
    for i,v in enumerate(arr):
        if cnt1==0 and v!=ele2:
            ele1=v
            cnt1+=1
        elif cnt2==0 and v!=ele1:
            ele2=v
            cnt2+=1
        elif ele1==v:
            cnt1+=1
        elif ele2 ==v:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    for i,v in enumerate(arr):
        if v==ele1:
            check_count1+=1
        if v==ele2:
            check_count2+=1
    if check_count2 > (len(arr)/3) and check_count1 > (len(arr)/3):
        return [ele1,ele2]
    return -1

'''
Time Complexity : O(N) + O(N)
Space Complexity : O(1)
'''


if __name__ == "__main__":
    arr = [1,1,1,2,2,2,12,1,1]
    # print(majority_element_better(arr))
    print(majority_element_optimal(arr))
