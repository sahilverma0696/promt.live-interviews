"""
122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] 
is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Input: prices = [7,1,5,3,6,4]
Output: 7


[1,5,7]

1,7 = 6


1,5 = 4
5,7 = 2
    = 6

time  O(N) 
space O(1)

[1,5,1, 7]
     | | 
[5,4,3,2] = 0


[7,5,4]
   | | 
"""


def solution(array):
    if len(array) <= 1:
        return 0
    profit = 0  # 0
    
    for i in range(1,len(array)):
        profit += max(0, array[i] - array[i-1])  #  max(0, -1)

    return profit  # 0



