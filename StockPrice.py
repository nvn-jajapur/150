'''
Best Time to Buy and sell a stock such that you make highest profit.
Condition is such that you have to buy and then only sell the stock as in array order.

SUM = A + B Logic
'''
from typing import List
def stock_price(arr:[])->int:
    mini=arr[0] # let us assume, we have bought the stock at the first index 
    profit = 0
    for i in range(1,len(arr)):
        profit_made = arr[i]-mini
        profit = max(profit,profit_made)
        mini = min(mini,arr[i]) # check for the lowest value
    return profit

def topKFrequent( nums: List[int], k: int) -> List[int]:
        hashMap ={}
        ans =[]
        for i, v in enumerate (nums):
            hashMap[v]=hashMap.get(v,0)+1
        print(hashMap)
        for i,(key,value)in enumerate(hashMap.items()):
            if value>=k:
                ans.append(value)
        return ans
if __name__=="__main__":
    arr = [1,2,4,6,-2,-8]
    arr1 = [1,1,1,2,2,3]
    # print(stock_price(arr))
    print(topKFrequent(arr1,2))