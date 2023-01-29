"""

Find an element in a sorted array

is it necessary the element is in the array : Yes 
size of the array ? 10^5
-10^5 < value < 10^5
is there a duplication ? No


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
    return -1