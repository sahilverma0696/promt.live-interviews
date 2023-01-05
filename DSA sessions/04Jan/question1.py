"""
121. Best Time to Buy and Sell Stock
Kadane's algorithm

you are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to
buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.


Arr = [1,2,3,4,5]
Solution = 4 

Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,5,4,3]
Output: 0

Input: prices = [7]
Output: 0

No -ve values 


[1, 2, 3, 4, 5] 

    |  | 

2 for loops and get the best result 


O(N), O(1)
[7,1,5,3,6,4]

       | 

max profit = 5
Max val 6




input : [1,3,6,4]
         |   


"""

def solution(array):
    if len(array) <= 1:
        return 0
    maxval = -9999        #  6
    maxprofit = -9999     #  3

    for val in reversed(range(len(array))):
        maxprofit = max(maxprofit, maxval - val)  #  max (3, 6-1) = 5
        maxval = max(maxval, val)                 #  6
    
    return max(0, maxprofit)

