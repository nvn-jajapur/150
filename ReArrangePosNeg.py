

'''
Optimal approach is while iterating on the arr, take two pointers and place the pos's at 2*index pos and 
negatives at 2*i+1 pos
'''
def reArrangeEqualPosNegs(arr:[])->[]:
    temp=[None]*len(arr)
    posIndex=0
    negIndex=1
    for i,v in enumerate(arr):
        if (arr[i]>0):
            temp[posIndex]=v
            posIndex+=2
        else:
            temp[negIndex]=v
            negIndex+=2
    return temp
'''
Time Complexity : O(N)
Space Complexity : O(N)
'''

'''
Here follow the Brute force approach of taking a posArray and negArray
if pos's > neg's then add pos at the end of array after completion of equal no of +'s and -'s, viceversa
'''

def reArrangeNoEqualPosNegs(arr:[])->[]:
    posArray,negArray=[],[]
    for i,v in enumerate(arr):
        if v>0:
            posArray.append(v)
        else:
            negArray.append(v)
    if len(posArray)>len(negArray):
        for neg in range(len(negArray)):
            arr[2*neg] = posArray[neg]
            arr[2*neg+1]=negArray[neg]
        for rem in range(len(negArray)*2,len(posArray)):
            arr[rem]=posArray[rem]
    else:
        for pos in range(len(posArray)):
            arr[2*pos] = posArray[pos]
            arr[2*pos+1]=negArray[pos]
        for rem in range(len(posArray)*2,len(negArray)): # if pos's == neg's then this loop would not work
            arr[rem]=negArray[rem]
    return arr

'''
Time Complexity : O(N) + O(N/leftOvers) + O(leftOvers) => O(N) + O(N)
Space Complexity : O(N/2) + O(N/2)
'''

if __name__=="__main__":
    arrWithEqualPosNegs =[1,2,-1,3,-2,-1]
    arrWithNoEqualPosNegs = [1,2,-1,3,-2,-1]
    # print(reArrangeEqualPosNegs(arrWithEqualPosNegs))
    print(reArrangeNoEqualPosNegs(arrWithNoEqualPosNegs))
