"""
Check Palindrome 

Given a string str, check if the characters of string makes a 
Palindrome. By ignoring the special character,numbers and space.


str = "r3a^ce8ca7r"
return true

str = "ba5bb^le "
return false


"babble"
"elbbab"
"racecar"
"racecar"

"bab^ "
i = 1
j = 1

"""

def isPalindrome(str) :#"e"

    front = 0  
    rear = len(str)-1  # 10

    def isaplhabet(charecter) :
        if ord('a')<= ord(charecter) and ord('z') >= ord(charecter) :
            return True
        if ord('A')<= ord(charecter) and ord('Z') >= ord(charecter) :
            return True
        return False

    while front < rear :  # 5 < 5 
        if not isaplhabet(str[front]) :
            front += 1
            continue
        
        if not isaplhabet(str[rear]) :
            rear -= 1
            continue
        
        if str[front] != str[rear] :
            return False
        front += 1 
        rear -= 1
    
    return True