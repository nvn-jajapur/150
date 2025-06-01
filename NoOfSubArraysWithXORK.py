from collections import defaultdict
class NoOfSubArraysWithXORK:
    def sub_array_with_k(self,arr:[],k:int)->int:
        xr = 0
        count =0
        hashmap = defaultdict(int)
        hashmap[0]= 1
        for i,v in enumerate(arr):
            xr=xr^v
            x= xr^k ## Formula froim the Striver Video
            count += hashmap[x]
            hashmap[xr]+=1


        return count
if __name__=="__main__":
    arr=[4,2,2,6,4]
    noo = NoOfSubArraysWithXORK()
    print(noo.sub_array_with_k(arr,6))