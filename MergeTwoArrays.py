from typing import List
class Solution:
    def merge_two_arrays(self,arr1:[],arr2:[])->[]:
        n = len(arr2)        
        arr1 = arr1[:-n]
        m = len(arr1)
       
        left = m-1
        right = 0
        while( left >=0 and right <n):
            if (arr1[left]> arr2[right]):
                arr1[left],arr2[right] = arr2[right],arr1[left]
                left-=1
                right+=1
            else:
                break
        arr1.sort()
        arr2.sort()
        print(arr1,arr2)
        arr1.extend(arr2)
        print(arr1)
        return []

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:-n]
        left = len(nums1)-1
        right = 0
        while (left>=0 and right < n):
            if (nums1[left] > nums2[right]):
                nums1[left],nums2[right]= nums2[right],nums1[left]
                left-=1
                right+=1
            else:
                break
        nums1.sort()
        nums2.sort()
        nums1.extend(nums2)
        print(nums1)
'''

Time complexity : O(m * n)
'''

if __name__ == "__main__":
    arr1=[1,2,3,0,0,0]
    arr2=[2,5,6]
    sol = Solution()
    print(sol.merge(arr1,len(arr1),arr2,len(arr2)))
    # print(sol.merge_two_arrays(arr1,arr2))