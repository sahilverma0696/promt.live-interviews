// You are given a string s of lowercase English letters and
// a 2D integer array shifts where shifts[i] = [ starti, endi ].
// For every i, shift the characters in s from the index starti to the index endi(inclusive).
// Return the final string after all such shifts to s are applied.

// s = "abc",shifts = [ [ 0, 1 ], [ 1, 2 ], [ 0, 2 ] ] result = "cee" 
// abc -> bcc -> bdd -> cee
// range + sum shift 
// 
// s = "dztz", shifts = [ [ 0, 0 ], [ 1, 1 ] ] result = "eatz"



/*
shift  =  1
// 
 = "abc",shifts = [ [ 0, 1 ], [ 1, 2 ], [ 0, 2 ] ] result = "cee" 

line sweeping operation
each time i absorb a shift
    i update the line -> summation is happening each time 
[0,0,0]
[1,1,0]
[1,2,1]
[2,3,2]
abc 
cee

2 for loop
range n = size of shifts
shifts[i][0]...shifts[i][1]
[0,0,0,0]
[1,0,-1,0] ->[1,1,0,0]

[1,0,-1]
[1,1,-1]
[2,1,-1]
[2,3,2]

3 for loops 
next to each other 
for loop 1
    shifts -> 
        for loop 2 
            shifts[i][0]
            shifts[i][0]

summation loop 
    sum of the line

shift making in string 
time O(n)

space O(n)

*/
#include<string>
#include<vector>

using namespace std;

string shiftChar( string &s, vector<vector<int>> & shifts)
{
    if(s == "")
        return "";
    int size =  s.size();
    int start = 0, end =0;
    int maxChar = 26;
    vector<int> line(size+1,0);

    // making marks on the line
    for(vector<int> & vec: shifts){
        start = vec[0];
        end   = vec[1];

        line[start]++;
        if(end != line.size()-1)        // optimization 
            line [end+1]--;         
    }

    // summation of line 
    for (int i = 1;i<line.size();i++)
    {
        line[i]=(line[i]+line[i-1])%maxChar;
    }

    for(int i = 0;i<s.size();i++)
    {
        s = (s[i]-'a' +line[i])%maxChar + 'a';
    }
    // shrinking the loops contains loop 2->3
    int x = line[0]; 
    for(int i = 0;i<s.size();i++)
    {
        x =(x+line[i])%maxChar;
        s = (s[i]-'a' +line[i])%maxChar + 'a';
    }
    return s;
}