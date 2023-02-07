/*

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your 
serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized 
to a string and this string can be deserialized to the 
original tree structure.
*/

/*
                             9
                            / \
                           2  10 
                          / \ / \
                            7 8  
*/
// Serialization : 
//          [9,2,10,1,7,8,11]
//          [9,2,10,?,7,8,?,?,?,?,?]
// pos :    [1,2,3 , 4  ,5,6,  7 , 8  , 9  , 10 , 11 ] 
//          node is at i then it's left child will be at 2*i and right child 
//          will be 
//          at 2*i+1

//Deserialization : 
// We are at a node which at i 