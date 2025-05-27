'''
Best Time to Buy and sell a stock such that you make highest profit.
Condition is such that you have to buy and then only sell the stock as in array order.

SUM = A + B Logic
'''

def stock_price(arr:[])->int:
    mini=arr[0] # let us assume, we have bought the stock at the first index 
    profit = 0
    for i in range(1,len(arr)):
        profit_made = arr[i]-mini
        profit = max(profit,profit_made)
        mini = min(mini,arr[i]) # check for the lowest value
    return profit


if __name__=="__main__":
    arr = [1,2,4,6,-2,-8]
    print(stock_price(arr))