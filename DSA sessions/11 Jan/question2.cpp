// You are given a string s of lowercase English letters and an integer 
// array shifts of the same length.

// Call the shift() of a letter, the next letter in the alphabet, 
//(wrapping around so that 'z' becomes 'a').

// For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
// Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

// Return the final string after all such shifts to s are applied.


// s = "abc", shifts = [3,5,9] result= "rpl"
// s = "aaa", shifts = [1,2,3] result= "gfd"

/*
abc 
17,14,9

aaa
6,5,3

max value of shift 10^9

time O(n)
space O(1)


*/

#include<string>
#include<vector>

using namespace std;


string shiftString(string str,vector<int> shifts)
{
    if(str.size()==0 || shifts.size()==0)
        return str;
    
    int sum = 0;
    int maxChar = 26;

    for(int i = str.size()-1;i>=0;i--)
    {
        sum = (sum+(shifts[i])%maxChar)%maxChar;
        str[i] = (str[i]-'a'+sum)%maxChar + 'a';
    }

    return str;
    
}


