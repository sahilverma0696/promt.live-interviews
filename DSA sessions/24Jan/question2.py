"""
Given two strings str1 and str2.

Check if str1 is present in str2 as an anagram.
str1 is considered as a valid anagram if str1 is present as a 
anagram grouped in str2

str1 = abd str2 = abscsbfsbcassa
    100+22+4      +(20+12)*10+3 -100 
return true

str2 = abc str2 = anxvbafdc
return false
"""

def anagramExists(str1, str2) :
    if len(str1) > len(str2) :
        return False
    # abc   abdcdbca
    def get_ord_value(char) :
        return ord(char) - ord('a') + 1

    def calculateHash(str,index1 ):
        hash1 = 0
        multiplier = 1

        while index1 >= 0 :
            hash += multiplier*(get_ord_value(str[index1]))
            multiplier *= 10
        return hash
    
    hash1 = calculateHash(str1, len(str1)-1)  # 3+ 10*2+100*1 = 123
    hash2 = calculateHash(str2, len(str1)-1)  #  124
    
    if hash1 == hash2 : return True 
    index1 = 0
    index2 = len(str1)
    multi = 10*(len(str1)-1)   #100

    while index2 < len(str2) :
        hash2 = (hash2 - multi*(get_ord_value(str2[index1]) )) * 10 + get_ord_value(str2[index2])   
        # 124 = 100=24*10 = 240 + c
        if hash1 == hash2 : 
            return True
        index1 += 1
        index2 += 1
    
    return False


#################################### 
""" Post Interview Correct Solution"""
####################################
# Counter function creates frequncy map of given iterable object
from collections import Counter  
def anagramExists(s1, s2) :
    cntr = Counter(s1)       # Frequncy map of string1
    words = len(s1)
    match = 0        #Flag to check if all words are matched     

    for i in range(len(s2)):
        if s2[i] in cntr:
            if not cntr[s2[i]]: 
                match -= 1
            cntr[s2[i]] -= 1
            if not cntr[s2[i]]: match += 1

        if i >= words and s2[i-words] in cntr:
            if not cntr[s2[i-words]]: match -= 1
            cntr[s2[i-words]] += 1
            if not cntr[s2[i-words]]: match += 1

        if match == len(cntr):
            return True

    return False



