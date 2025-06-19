from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        i,j=0,0
        arr=[]
        while(i<n1 and j<n2):
            if(nums1[i] < nums2[j]):
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        while(i<n1):
            arr.append(nums1[i])
            i+=1
        while(j<n2):
            arr.append(nums2[j])
            j+=1
        x : int= len(arr)
        if ( x%2 ==1):
            return arr[x//2]
        else:
            return (arr[x//2] + arr[x//2 -1])/2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = (n1+n2)
        i,j=0,0
        index1 = (n//2)
        index2 =index1-1
        index1_ele,index2_ele =-1,-1
        count=0
        while(i<n1 and j<n2):
            if ( nums1[i] <nums2[j]):
                if(count == index1): 
                    index1_ele = nums1[i]
                if(count==index2):
                    index2_ele = nums1[i]
                i+=1
                count+=1
            else:
                if(count == index1):
                    index1_ele = nums2[j]
                if(count == index2):
                    index2_ele = nums2[j]
                j+=1
                count+=1
        while(i<n1):
            if(count == index1): 
                index1_ele = nums1[i]
            if(count==index2):
                index2_ele = nums1[i]
            i+=1
            count+=1
        while(j<n2):
            if(count == index1):
                index1_ele = nums2[j]
            if(count == index2):
                index2_ele = nums2[j]
            j+=1
            count+=1
        if(n%2 ==1): return index1_ele
        else: return (index1_ele + index2_ele)/2
        
if __name__ == '__main__':
    arr1=[1,2]
    arr2 =[3]
    sol = Solution()
    # print(sol.findMedianSortedArrays(arr1,arr2))
    print(sol.findMedianSortedArrays(arr1,arr2))