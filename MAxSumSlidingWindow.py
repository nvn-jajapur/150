def max_sum (arr:[], k:int)->int:
    left = right = length = sum =0
    while(right < len(arr)-1):
        sum += arr[right]
        if ( sum > k):
            sum -= arr[left]
            left +=1
        if( sum <=k):
            length = max(length, right -left + 1)
        right +=1
        
    return length

if __name__ =='__main__':
    arr = [2,5,1,10,10]
    print(max_sum(arr,14))



