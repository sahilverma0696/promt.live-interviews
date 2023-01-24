"""

// Given two inputs,

// First input is the location map, a 2D array

// | O | E | E | E | X | 
// | E | O | X | X | X |
// | E | E | E | E | E |
// | X | E | O | E | E |
// | X | E | X | E | X | 

// O = Robot, E = Empty, X = blocker

// Second input is the query. It’s a 1D array consisting of distance to the closest blocker
 in the order from left, top, bottom and right

// [2, 2, 4, 1] -> This means distance of 2 to the left blocker, 2 to the top blocker,
 4 to the bottom blocker and 1 to the right blocker

// Note: The location map boundary is also considered blocker, 
meaning if the robot hits the boundary it also means it’s hitting the blocker.

// Write a function that takes these two inputs and returns the index of the robots 
(if any) that matches the query that we’re looking for.

// Solution for the example above would be the robot located at index [1, 1]

Left Top bottom and Right 


// | O | E | E | E | X | 
// | E | O | X | X | X |
// | E | E | E | E | E |
// | X | E | O | E | E |
// | X | E | X | E | X | 

/*

// | O | E | E | E | X | 
// | E | O | X | X | X |
// | E | E | E | E | E |
// | X | E | O | E | E |
// | X | E | X | E | X | 

[2, 2, 4, 1]

// X   X   X   X
// X | O | E | 3
// X | E | O | 3
// X | 1 | E | 2
   X   X   X   X
 2 ways i am thinking 
 Compute with each Bot 
 Compute with each Blocker


X  ....O.....  X  (left, right)    (left + right, 0)    


(left, top,bottom, right)



"""


def GridQuery(grid, query):
    left,top,bottom,right = query
    lr = left + right
    tb = top + bottom
    res = list()

    x,y = len(grid[0]), len(grid)

    LRDP = [[0 for _ in range(x+2)] for _ in range(y+2)]

    for row_number, row_values in enumerate(grid):
        obstacle_distance = 1
        for col_number, value in enumerate(["X"] + row_values + ["X"]):
            if value == "X":
                LRDP[row_number][col_number] = obstacle_distance
                obstacle_distance = 0
            obstacle_distance += 1

    for col_number, col_value in enumerate(zip(grid)):
        obstacle_distance = 1
        for row_number, row_values in enumerate(["X"] + col_value + ["X"]):
            if value == "X":
                if obstacle_distance == tb:
                    pos_bot = (row_number - bottom, col_number)
                    if grid[pos_bot[0], pos_bot[1]] == "0":
                        # check for obstacle right distnce away 
                        pos_obstacle = (pos_bot[0], pos_bot[1] + right)
                        if grid(pos_obstacle) == lr:
                            res.append(pos_bot)
                




 

        
            

                


    
