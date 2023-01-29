"""
Search & count in 2d matrix, duplicates allowed

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.


New conditions:     
                    duplicates will be present 
                    count of number times the value existed
completely unique 3 -> only once 
[non-decreasing ]


Input: matrix = [   [1,3,5,7,7,7],
                    [7,11,16,20,20,20],
                    [23,30,34,60,60,60]
                ], target = 3
Output: true
"""
"""
Time N
Space 1 
"""




def binarysearchLeft(arr, value):
    if arr == []:
        return -1

    start,end = 0, len(arr) * len(arr[0])-1
    last_occurence = -1
    
    while start <= end:
        mid = (start + end)//2  
        value_mid = getvaluefrommatrix(arr, mid)
        if value_mid == value:
            end = mid - 1  
            last_occurence = mid    
        elif value_mid < value:
            start = mid + 1        
        else:  # value_mid > value
            end = mid - 1
    return last_occurence

def binarysearchRight(arr, value):
    if arr == []:
        return -1

    start,end = 0, len(arr) * len(arr[0])-1
    last_occurence = -1
    while start <= end:
        mid = (start + end)//2  
        value_mid = getvaluefrommatrix(arr, mid)
        if value_mid == value:
            start = mid + 1
            last_occurence = mid    
        elif value_mid < value:
            start = mid + 1        
        else:  # value_mid > value
            end = mid - 1
    return last_occurence

def getvaluefrommatrix(matrix, index):
    row_length = len(matrix)
    x,y = index//row_length, index%row_length

    return matrix[x][y]

def Solution(matrix, value):
    start = binarysearchLeft(matrix, value)
    if start == -1:
        return 0

    end = binarysearchRight(matrix, value)

    return end - start + 1