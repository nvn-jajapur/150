def allocate_books(arr:[], m : int):
    low = max(arr)
    high  = sum(arr)
    for i in range(low,high):
        x = check(arr,i)
        if (x ==m):
            return i
    
def check(arr:[], m : int):
    sum =0
    no_of_students =1
    for i in arr:
        if ( (sum + i) <= m ):
            sum +=i
        else:
            sum =i
            no_of_students +=1
    return no_of_students

def allocate_books_bs(arr:[], m:int):
    low = max(arr)
    high = sum(arr)
    while(low <= high):
        mid =(low + high)//2
        x = check(arr,mid)
        if x>m: low = mid+1
        else: high = mid-1
    return low

if __name__ =="__main__":
    arr = [1,4,8,10,20]
    # print(allocate_books(arr,4))
    print(allocate_books_bs(arr,3))