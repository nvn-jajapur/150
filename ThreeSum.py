def three_sum(arr:[])->[]:
    ans_set= set()
    for i in range(len(arr)):
        hashSet = set()
        for j in range(i+1, len(arr)):
            third = - (arr[i] +arr[j])
            if third in hashSet:
                temp = [arr[i], arr[j], third]
                temp.sort()
                ans_set.add(tuple(temp))
            hashSet.add(arr[j])
    return list(ans_set)
''''
Time Complexity : O(N2) * O(NlogN)
Space Complexity : O(N)
'''

def three_sum_optimal(arr:[])->[]:
    ans = []
    arr.sort()
    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue
        j = i + 1
        k = len(arr)-1
        while(j<k):
            sum = arr[i] + arr[j] + arr[k]
            if (sum>0):
                k-=1
            elif sum<0:
                j+=1
            else:
                temp = [arr[i], arr[j], arr[k]]
                j+=1
                k-=1
                ans.append(temp)
                while (j<k and arr[j] == arr[j-1]):
                    j+=1
                while ( j<k and arr[k] == arr[k+1]):
                    k-=1
                
    return ans

''''
Time Complexity : O(N2) * O(NlogN)
Space Complexity : O(Temp)
'''
if __name__ == '__main__':
    arr = [1,-1,-2,0,2,1,-1]
    print(three_sum(arr))
    print(three_sum_optimal(arr))


