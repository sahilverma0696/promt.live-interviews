"""
Leetcode : 2400. Number of Ways to Reach a Position After Exactly k Steps

You are given two positive integers startPos and endPos. 
Initially, you are standing at position startPos on an infinite number line. 
With one step, you can move either one position to the left, or one position to the right.

Given a positive integer k, return the number of different ways to 
reach the position endPos starting from startPos, such that you perform exactly k steps. 
Since the answer may be very large, return it modulo 10^9 + 7.

Two ways are considered different if the order of the steps made is not exactly the same.

Note that the number line includes negative integers.


Input: startPos = 1, endPos = 2, k = 3
Output: 3
Explanation: We can reach position 2 from 1 in exactly 3 steps in three ways:
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
It can be proven that no other way is possible, so we return 3.




startPos            endPos

   ^                  ^  

        x-1     x     x+1   x+2
                ^
        ^              ^
^               ^           ^


startPos = 1, endPos = 10,  k = 2

"""

# startPos = 1, endPos = 2, k = 3

dp = {} # Hashmap 

def KJumpstep(startPos, endPos, k):
    
    # when we reach a position and check k's remaining is zero we check if we got ot destination 
    if k == 0:
        return 1 if startPos == endPos else 0

    # number of jumps remaining < distance to be covered 

    if abs(startPos - endPos) > k:
        return 0

    # have we computed it so we can give that information back 
    if (startPos, k) in dp:
        return dp(startPos, k)

    jump_left = KJumpstep(startPos - 1, endPos, k - 1)
    jump_right = KJumpstep(startPos + 1, endPos, k - 1)

    total_pos = jump_left + jump_right

    dp[(startPos, k)] = total_pos

    return dp[(startPos, k)] 
    
"""
KJumpstep(1,2,3)
    JL = KJumpstep(0,2,2) #  - 1 -> 0 -> 1 -> 2.
    JR = KJumpstep(2,2,2) # - 1 -> 2 -> 3 -> 2.  # - 1 -> 2 -> 1 -> 2.


KJumpstep(0,2,2)
    JL = 0 #
    JR = 1

KJumpstep(1,2,1)
    JL = 0
    JR = 1



"""