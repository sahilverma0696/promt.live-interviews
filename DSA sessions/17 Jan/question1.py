"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


n         ---------
              |   |  
n - 1     ----    |      
                  |  
n - 2     ---------      

F(n) = F(n-1)+F(n-2)


"""

def stairs(stair):
    if stair <= 0:
        return 0

    return stairs_recursive(stair)



def stairs_recursive(stair):
    if stair == 0:
        return 1
    elif stair < 0:
        return 0

    # jump from n - 1 stairs

    first_possiblity = stairs_recursive(stair - 1)

    # jump from n - 1 stairs
    second_possiblity = stairs_recursive(stair - 2)

    # sum of both possiblity 

    total_possiblity  = first_possiblity + second_possiblity

    return total_possiblity 

"""

stairs_recursive(2):
    first_pos = 1
    second_pos = 1
    return 1 + 1

stairs_recursive(1)
    first_pos = 1
    second_pos = 0
    return 1 + 0


"""