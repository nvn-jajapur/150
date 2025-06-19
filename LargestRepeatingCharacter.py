def sub_array_with_dfrnt_integers(arr:[],k:int):
    l = r = count=0
    mpp={}
    while( r < len(arr)):
        mpp[arr[r]] = mpp.get(arr[r],0)+1
        while( len(mpp) >k):
            mpp[arr[l]] = mpp.get(arr[l],0)-1
            if(mpp[arr[l]] ==0):
                mpp.pop(arr[l])
            l+=1
        count+=(r-l+1)
        r+=1
    return count 

if __name__ == '__main__':
    arr = [1,2,1,3,4]
    x = sub_array_with_dfrnt_integers(arr,3)
    y = sub_array_with_dfrnt_integers(arr,2)
    print(x-y)