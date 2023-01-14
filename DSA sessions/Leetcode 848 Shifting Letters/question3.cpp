/*
You are given a string s of lowercase English letters and a 2D 
integer array shifts where shifts[i] = [ starti, endi ].
For every i, shift the characters in s from the index starti to the index endi(inclusive).
Return the final string after all such shifts to s are applied.
 s = "abc", shifts = [ [ 0, 1 ], [ 1, 2 ], [ 0, 2 ] ] result = "cee" 
 s = "dztz", shifts = [ [ 0, 0 ], [ 1, 1 ] ] result = "eatz"
*/

/*
shift = 1, to the right
s = "abc", shifts = [ [ 0, 1 ], [ 1, 2 ], [ 0, 2 ] ] result = "cee"

a b c
b c c
b d d
c e e


time complexity of the same
// make the code more verbose

a b c
0 0 0
1 1 0   -> 0, 1
1 2 1   -> 1, 2 
2 3 2
a b c
c e e

2 for loops
    shifts
        shifts[i] ->

O(n) size of shifts

O(n^2) in case of updating the line each iteration

[ [ 0, 1 ], [ 1, 2 ], [ 0, 2 ] ]
a b c
0 0 0  0
1 0 -1 0
1 1 -1 -1
2 1 -1 -2
2 3 2 0
a b c
c e e



for each shift in shifts
    shift[0] = starting
    shift[1] = ending

    in my line
        line[starting] + 1
        line[ending+1] - 1

sum increasing from left to right
which gives me the array of each shift needed to be made

time O(n)
space O(n)


*/

#include<string>
#include<vector>

using namespace std;

string shiftChar(string str, vector<vector<int>> shifts)
{
    if(str.size()==0 || shifts.size()==0)
        return str;

    int size = str.size();
    vector<int> line(size+1,0);

    int start = 0;
    int end = 0;
    int maxChar =  26;

    // for loop to mark the starting and ending values of shift 
    for(vector<int> &vec: shifts)
    {
        start = vec[0];
        end   = vec[1]+1;

        line[start] = (line[start]+1)%maxChar;
        line[end]   = (line[end]-1)%maxChar;
    }

    // // make the sum from left to right in line 

    // for (int i = 1;i<line.size();i++)
    // {
    //     line[i] =(line[i]+line[i-1])%maxChar;
    // }

    // // makes the transformation in the string 
    // for(int i = 0;i<str.size();i++)
    // {   
    //     str[i] = (str[i]-'a' + line[i])%maxChar + 'a';
    // }

    int sum  = 0;
    for(int i = 0;i<str.size();i++)
    {
        sum =(sum+line[i])%maxChar;  // safeguard enabled 
        str[i] = (str[i]-'a' +sum)%maxChar + 'a';
    }

    return str;
    
}