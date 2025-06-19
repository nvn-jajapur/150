def max_sub_arrauy_product(arr)->int:
    ans=0
    n=len(arr)
    prefix, suffix = 1,1

    for i in range(len(arr)):
        if prefix ==0:
            prefix = 1
        if suffix ==0:
            suffix=1
        prefix = prefix*arr[i]
        suffix = suffix * arr[n-i-1]
        ans = max ( ans, max(prefix,suffix))
    return  ans

if __name__ =='__main__':
    lst = [-2,3,4,-1,0,-2,3,1,4,0,4,6,-1,4]
    print(max_sub_arrauy_product(lst))