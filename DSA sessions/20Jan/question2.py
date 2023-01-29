"""
Leetcode : 74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

completely unique 3 -> only once 
[non-decreasing ]


Input: matrix = [   [1,3,5,7],
                    [10,11,16,20],
                    [23,30,34,60]
                ], target = 3
Output: true
"""


def binarysearch(arr, value):
    if arr == []:
        return -1

    start,end = 0, len(arr)-1
    
    while start <= end:
        mid = (start + end)//2  ## start +(end-start)/2
        value_mid = arr[mid] 
        if value_mid == value:
            return mid        
        elif value_mid < value:
            start = mid + 1        
        else:  # value_mid > value
            end = mid - 1
    return end

# [ [1,3,5,7],
#   [10,11,16,20],
#   [23,30,34,60]
# ], target = 3

def Solution(matrix, value):
    row_count = len(matrix)
    col_count = len(matrix[0])

    row_numbers = [row[0] for row in matrix] # [1,10,23]  in normal code we can write a
                                             # binary search for the row as seperate entity 
    indexrow = binarysearch(row_numbers)  # 0
    indexcolumn = binarysearch(matrix[indexrow]) # 1

    if indexcolumn >= col_count:
        return False

    return matrix[indexrow][indexcolumn]  == value 




    


