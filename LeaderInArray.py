'''
This is the optimal approach, start from the back and check for the max from right,
because if if you find a max ele, the right elements should be min than max element
'''

def leader_in_array(arr:[])->[]:
    temp=[]
    maxi=arr[len(arr)-1]
    temp.append(maxi)
    for i in range(len(arr)-1,0,-1):
        if ( arr[i]>maxi):
            temp.append(arr[i])
            maxi=max(maxi,arr[i])
    temp.sort() # if the sorted order is asked
    return temp
"""
Time Complexity : O(NlogN) -> as we are sorting, else O(N)
Space Complexity : O(N)
"""

        


if __name__=="__main__":
    arr = [10,22,12,3,0,6]
    print(leader_in_array(arr))