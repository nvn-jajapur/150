def stock_price(arr:[])->int:
    mini=arr[0]
    profit=0
    for i in range(1,len(arr)):
        profit_made = arr[i]- mini
        profit = max(profit, profit_made)
        mini = min(mini,arr[i])
    return profit


if __name__=="__main__":
    arr = [1,-2,4,6,-2,-8]
    print(stock_price(arr))